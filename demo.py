#!/usr/bin/env python3
"""
EMERALD_PYGAME Demo - Run from project root
Usage: python demo.py
"""

import sys
from pathlib import Path

# Add src to path so imports work
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data.loader import validate_data, get_species, get_move
from models import create_pokemon, create_player, create_gym_leader, get_move_obj_by_name
from engines import BattleEngine, BattleAction, ActionType


def demo_data():
    """Test data loading."""
    print("=" * 60)
    print("DATA VALIDATION")
    print("=" * 60)
    
    counts = validate_data()
    for name, count in counts.items():
        status = "✓" if count > 0 else "✗"
        print(f"  {status} {name}: {count}")
    
    # Sample lookups
    bulbasaur = get_species(1)
    print(f"\nBulbasaur: {bulbasaur['types']}, HP={bulbasaur['base_stats']['hp']}")
    
    flamethrower = get_move_obj_by_name("flamethrower")
    print(f"Flamethrower: {flamethrower.type}, Power={flamethrower.power}")


def demo_pokemon():
    """Test Pokemon creation."""
    print("\n" + "=" * 60)
    print("POKEMON CREATION")
    print("=" * 60)
    
    pokemon_list = [
        (1, 5, "Bulbasaur"),
        (6, 50, "Charizard"),
        (25, 30, "Pikachu"),
        (150, 70, "Mewtwo"),
    ]
    
    for species_id, level, expected_name in pokemon_list:
        p = create_pokemon(species_id, level=level)
        print(f"  {p.name} Lv.{p.level}: {p.types}, HP={p.max_hp}, Ability={p.ability}")


def demo_battle():
    """Run a sample battle."""
    print("\n" + "=" * 60)
    print("BATTLE DEMO")
    print("=" * 60)
    
    # Create player
    player = create_player("Red")
    charizard = create_pokemon(6, level=50)  # Charizard
    charizard.learn_move(53)   # Flamethrower
    charizard.learn_move(89)   # Earthquake
    player.add_pokemon(charizard)
    
    # Create opponent
    opponent = create_gym_leader("Brock", "Gym Leader")
    geodude = create_pokemon(74, level=25)  # Geodude
    geodude.learn_move(89)   # Earthquake
    geodude.learn_move(88)   # Rock Throw
    opponent.add_pokemon(geodude)
    
    print(f"\n{player.name}'s {charizard.name} Lv.{charizard.level}")
    print(f"  vs")
    print(f"{opponent.name}'s {geodude.name} Lv.{geodude.level}")
    print(f"\nHP: {charizard.current_hp} vs {geodude.current_hp}")
    
    # Start battle
    battle = BattleEngine(player, opponent, is_wild=False)
    
    # Turn 1: Charizard uses Flamethrower
    print("\n--- Turn 1 ---")
    print("Charizard uses Flamethrower!")
    
    p_action = BattleAction(
        action_type=ActionType.FIGHT,
        user=battle.state.player_pokemon,
        trainer=player,
        move_id=53,  # Flamethrower
        move_slot=0,
    )
    
    o_action = BattleAction(
        action_type=ActionType.FIGHT,
        user=battle.state.opponent_pokemon,
        trainer=opponent,
        move_id=89,  # Earthquake
        move_slot=0,
    )
    
    battle.execute_turn(p_action, o_action)
    
    # Show results
    print("\nBattle events:")
    for event in battle.state.log:
        t = event.get("type")
        if t == "damage":
            print(f"  {event['target']} took {event['damage']} damage!")
        elif t == "super_effective":
            print(f"  It's super effective! ({event['multiplier']}x)")
        elif t == "not_very_effective":
            print(f"  It's not very effective... ({event['multiplier']}x)")
        elif t == "immune":
            print(f"  {event['defender']} is immune!")
        elif t == "faint":
            print(f"  {event['pokemon']} fainted!")
        elif t == "critical_hit":
            print(f"  Critical hit!")
    
    print(f"\nFinal HP:")
    print(f"  {charizard.name}: {charizard.current_hp}/{charizard.max_hp}")
    print(f"  {geodude.name}: {geodude.current_hp}/{geodude.max_hp}")
    
    if battle.state.ended:
        winner = battle.state.winner
        print(f"\n{'='*20}")
        print(f"Winner: {winner.name if winner else 'None'}!")


def demo_type_effectiveness():
    """Show type effectiveness in action."""
    print("\n" + "=" * 60)
    print("TYPE EFFECTIVENESS")
    print("=" * 60)
    
    moves = [
        ("Thunderbolt", ["Water"]),
        ("Thunderbolt", ["Ground"]),
        ("Flamethrower", ["Grass", "Steel"]),
        ("Earthquake", ["Fire", "Flying"]),
    ]
    
    for move_name, defender_types in moves:
        move = get_move_obj_by_name(move_name)
        eff = move.get_effectiveness(defender_types)
        print(f"  {move_name} vs {defender_types}: {eff}x")


def demo_ai():
    """Demonstrate AI decision-making."""
    print("\n" + "=" * 60)
    print("AI DECISION-MAKING")
    print("=" * 60)
    
    from engines.ai import TrainerAI
    from engines.ai_scoring import score_all_moves
    from engines.battle_pokemon import wrap_for_battle
    
    # Setup: Gym Leader with items
    opponent = create_gym_leader("Brock", "Gym Leader")
    steelix = create_pokemon(208, level=50)  # Steel/Ground
    steelix.learn_move(89)   # Earthquake
    steelix.learn_move(231)  # Iron Tail
    steelix.learn_move(157)  # Rock Slide
    opponent.add_pokemon(steelix)
    opponent.add_item(21, 2)  # 2 Hyper Potions
    
    player = create_player("Red")
    charizard = create_pokemon(6, level=50)  # Fire/Flying
    charizard.learn_move(53)   # Flamethrower
    charizard.learn_move(89)   # Earthquake
    player.add_pokemon(charizard)
    
    battle = BattleEngine(player, opponent)
    ai = TrainerAI(opponent)
    
    # Show move scoring
    print("\n1. Move Scoring (Steelix vs Charizard):")
    scores = score_all_moves(
        battle.state.opponent_pokemon,
        battle.state.player_pokemon,
        battle.state,
        opponent.ai_flags,
    )
    
    from data.loader import get_move
    for slot, move_id, score in scores:
        move = get_move(move_id)
        print(f"   {move['name']}: score {score}")
    
    # Show AI choice
    print("\n2. AI Decision (Full HP):")
    action = ai.choose_action(battle.state, battle.state.opponent_pokemon, battle.state.player_pokemon)
    print(f"   Action: {action.action_type.name}")
    if action.move_id:
        print(f"   Move: {get_move(action.move_id)['name']}")
    
    # Damage to trigger healing
    print("\n3. AI Decision (Low HP - 20%):")
    steelix.current_hp = int(steelix.max_hp * 0.2)
    battle.state.opponent_pokemon = wrap_for_battle(steelix)
    print(f"   Steelix HP: {steelix.current_hp}/{steelix.max_hp}")
    
    action = ai.choose_action(battle.state, battle.state.opponent_pokemon, battle.state.player_pokemon)
    print(f"   Action: {action.action_type.name}")
    if action.item_id:
        from models.item import get_item_obj
        item = get_item_obj(action.item_id)
        print(f"   Item: {item.name}")


def demo_overworld():
    """Demonstrate overworld system."""
    print("\n" + "=" * 60)
    print("OVERWORLD SYSTEM")
    print("=" * 60)
    
    from engines.map_engine import MapEngine, MoveResult
    from engines.encounters import EncounterSystem
    from models.player import Player, Direction
    
    # Create map engine and load Littleroot
    engine = MapEngine()
    
    print("\n1. Available Maps:")
    for name in engine.maps_data.keys():
        print(f"   - {name}")
    
    # Load Littleroot Town
    print("\n2. Loading Littleroot Town...")
    map_data = engine.load_map("littleroot_town")
    if map_data:
        print(f"   Name: {map_data.name}")
        print(f"   Size: {map_data.width}x{map_data.height}")
        print(f"   Warps: {len(map_data.warps)}")
        print(f"   NPCs: {len(map_data.npcs)}")
    
    # Create player and test movement
    print("\n3. Player Movement Test:")
    player = Player(x=10, y=10, facing=Direction.SOUTH)
    print(f"   Start: ({player.x}, {player.y})")
    
    # Move south
    result = engine.move_player(player, Direction.SOUTH)
    print(f"   Move SOUTH: {result.name} → ({player.x}, {player.y})")
    
    # Move east
    result = engine.move_player(player, Direction.EAST)
    print(f"   Move EAST: {result.name} → ({player.x}, {player.y})")
    
    # Load Route 101 for encounters
    print("\n4. Wild Encounter Test (Route 101):")
    engine.load_map("route_101")
    print(f"   Map: {engine.current_map.name}")
    print(f"   Encounter rate: {engine.current_map.encounter_rate}%")
    print(f"   Encounter table:")
    
    from data.loader import get_species
    for e in engine.current_map.encounter_table:
        species = get_species(e.species_id)
        name = species['name'] if species else f"#{e.species_id}"
        print(f"      {name} Lv.{e.min_level}-{e.max_level} ({e.rate}%)")
    
    # Test encounter generation
    print("\n5. Simulating Encounters (100 steps):")
    encounters = {}
    for _ in range(100):
        result = engine.get_wild_pokemon()
        if result:
            species_id, level = result
            species = get_species(species_id)
            name = species['name'] if species else f"#{species_id}"
            key = f"{name} Lv.{level}"
            encounters[key] = encounters.get(key, 0) + 1
    
    if encounters:
        for name, count in sorted(encounters.items()):
            print(f"      {name}: {count}")
    else:
        print("      (No encounters in this simulation)")
    
    # Test warp
    print("\n6. Warp Test:")
    warp = engine.current_map.warps[0] if engine.current_map.warps else None
    if warp:
        print(f"   Warp at ({warp.x}, {warp.y}) → {warp.dest_map} ({warp.dest_x}, {warp.dest_y})")


def demo_scripts():
    """Demonstrate script system."""
    print("\n" + "=" * 60)
    print("SCRIPT SYSTEM")
    print("=" * 60)
    
    from systems.game_state import GameState, FLAG_RECEIVED_STARTER
    from engines.script_vm import ScriptVM, ScriptState
    from models.player import Player
    
    # Create fresh state
    game_state = GameState()
    player = Player(name="Red")
    script_vm = ScriptVM(game_state, player)
    
    # Collect messages for display
    messages = []
    def on_msg(msg):
        messages.append(msg.text)
    script_vm.on_message = on_msg
    
    # Test script: Simple dialogue
    print("\n1. Simple Dialogue:")
    test_script = [
        {"cmd": "msgbox", "text": "Hello, {PLAYER}!"},
        {"cmd": "msgbox", "text": "Welcome to the world of POKEMON!"},
        {"cmd": "end"}
    ]
    
    script_vm.run_script("test", test_script)
    
    while script_vm.state != ScriptState.IDLE:
        script_vm.update()
        if script_vm.state == ScriptState.WAITING_TEXT:
            script_vm.dismiss_message()
    
    for msg in messages:
        print(f"   \"{msg}\"")
    messages.clear()
    
    # Test: Give Pokemon
    print("\n2. Give Pokemon Script:")
    give_script = [
        {"cmd": "msgbox", "text": "Here's a TREECKO!"},
        {"cmd": "givepokemon", "species": 252, "level": 5},
        {"cmd": "setflag", "flag": 1},
        {"cmd": "end"}
    ]
    
    script_vm.run_script("give", give_script)
    
    while script_vm.state != ScriptState.IDLE:
        script_vm.update()
        if script_vm.state == ScriptState.WAITING_TEXT:
            script_vm.dismiss_message()
    
    for msg in messages:
        print(f"   \"{msg}\"")
    
    print(f"   Party size: {len(player.party)}")
    if player.party:
        print(f"   Pokemon: {player.party[0].name} Lv.{player.party[0].level}")
    print(f"   FLAG_RECEIVED_STARTER: {game_state.check_flag(FLAG_RECEIVED_STARTER)}")
    
    # Test: Flags and Vars
    print("\n3. Flag/Variable System:")
    game_state.give_badge(1)
    game_state.give_badge(2)
    game_state.set_var(0x02, 252)  # Starter choice = Treecko
    
    print(f"   Badges: {game_state.badge_count}")
    print(f"   Has Badge 1: {game_state.has_badge(1)}")
    print(f"   Has Badge 3: {game_state.has_badge(3)}")
    print(f"   VAR_STARTER_CHOICE: {game_state.get_var(0x02)}")


def demo_pygame():
    """Demonstrate Pygame views (if available)."""
    print("\n" + "=" * 60)
    print("PYGAME VIEWS")
    print("=" * 60)
    
    try:
        import pygame
        PYGAME_AVAILABLE = True
        print("\n  Pygame version:", pygame.version.ver)
    except ImportError:
        PYGAME_AVAILABLE = False
        print("\n  Pygame not installed - skipping visual demo")
        print("  Install with: pip install pygame")
        return
    
    print("  Native resolution: 240x160 (GBA)")
    print("  Scale: 3x (720x480 window)")
    print("\n  View modules created:")
    print("   - GameWindow (window.py)")
    print("   - BattleView (battle_view.py)")
    print("   - OverworldView (overworld_view.py)")
    print("   - DialogueBox (dialogue.py)")
    print("   - Game (game.py)")
    
    print("\n  To run the graphical game:")
    print("   python -c \"from src.views.game import main; main()\"")
    print("  Or:")
    print("   python src/views/game.py")


def main():
    print("\n" + "=" * 60)
    print("   EMERALD_PYGAME - Demo")
    print("   Pokemon Emerald Clean-Room Reimplementation")
    print("=" * 60)
    
    demo_data()
    demo_pokemon()
    demo_type_effectiveness()
    demo_ai()
    demo_overworld()
    demo_scripts()
    demo_pygame()
    demo_battle()
    
    print("\n" + "=" * 60)
    print("✓ All demos completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
