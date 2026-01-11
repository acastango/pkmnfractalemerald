#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
EMERALD FLOW DEMO: The Strange Loop in Action
═══════════════════════════════════════════════════════════════════════════════

This demo shows the complete Strange Loop system:
- Oscillator dynamics (Domain 2)
- Flow meters (Domain 1-3)
- Social Pokemon with trust mechanics (Domain 3)
- The causal feedback loop

Run with: python demo_strange_loop.py
"""

import sys
sys.path.insert(0, 'src')

from models.pokemon import create_pokemon, Nature
from models.social_pokemon import (
    wrap_pokemon_social, TrainerDecision, BattleEvent, verify_strange_loop
)
from systems.flow_engine import FlowEngine, create_party_flow_engine
from systems.oscillator import Oscillator, get_nature_frequency
from systems.social_memory import SocialMemory


def print_header(text: str):
    print()
    print("═" * 60)
    print(f"  {text}")
    print("═" * 60)


def print_subheader(text: str):
    print()
    print(f"── {text} ──")


def demo_oscillator_synchronization():
    """Demonstrate Kuramoto dynamics leading to phase-lock."""
    print_header("DEMO 1: Oscillator Synchronization")
    
    print("\nCreating 3 oscillators with different initial phases...")
    engine = FlowEngine(base_coupling=0.3)
    
    # Three Pokemon with different natures
    natures = ['ADAMANT', 'TIMID', 'CALM']
    for i, nature in enumerate(natures):
        osc = Oscillator(
            entity_id=f"Pokemon_{i+1}",
            theta=i * 2.0,  # Different starting phases
            omega=get_nature_frequency(nature),
            amplitude=1.0,
        )
        engine.add_oscillator(osc)
        print(f"  {osc.entity_id}: θ={osc.theta:.2f}, ω={osc.omega:.2f} ({nature})")
    
    print(f"\nInitial order parameter r: {engine.order_parameter:.3f}")
    print(f"State: {engine.get_coherence_state()}")
    
    print("\nSimulating 50 time steps...")
    for step in range(50):
        engine.step()
        if step % 10 == 9:
            print(f"  Step {step+1}: r = {engine.order_parameter:.3f}")
    
    print(f"\nFinal order parameter r: {engine.order_parameter:.3f}")
    print(f"State: {engine.get_coherence_state()}")
    
    if engine.order_parameter > 0.7:
        print("\n✓ Party achieved PHASE-LOCK!")
        print("  The oscillators are synchronized. Flow can build.")


def demo_flow_building():
    """Demonstrate flow building through good play."""
    print_header("DEMO 2: Flow Building Through Good Play")
    
    # Create a Pokemon
    pokemon = create_pokemon(species_id=257, level=50, nature=Nature.ADAMANT)  # Blaziken
    social = wrap_pokemon_social(pokemon, unique_id="blaziken_001")
    
    print(f"\n{pokemon.name} (ADAMANT Nature)")
    print(f"  Initial Flow: {social.flow:.0%}")
    print(f"  Flow Ceiling: {social.flow_ceiling:.0%}")
    print(f"  Trainer Trust: {social.social.trainer_trust:.2f}")
    
    print_subheader("Simulating a battle with good play")
    
    # Simulate dealing damage
    damages = [45, 52, 61, 48, 55, 60, 42, 58]  # Good damage sequence
    
    for i, damage in enumerate(damages):
        social.on_move_resolved(i, damage, was_crit=False)
        
        if (i + 1) % 3 == 0:  # Check every 3 moves
            print(f"  After move {i+1}: Flow = {social.flow:.1%}, Tier = {social.flow_meter.tier_name}")
        
        # Also update trust for good play
        social.update_trainer_trust(TrainerDecision.OPTIMAL_MOVE)
    
    print(f"\nFinal Flow: {social.flow:.1%}")
    print(f"Damage Multiplier: {social.get_damage_multiplier():.2%}")
    print(f"Nature Bonuses: {social.flow_meter.get_nature_bonuses()}")


def demo_strange_loop():
    """Demonstrate the complete Strange Loop."""
    print_header("DEMO 3: THE STRANGE LOOP")
    
    print("""
    The Loop:
    ┌─────────────────────────────────────────────────────┐
    │  Player Input                                       │
    │      ↓                                              │
    │  BattleEngine executes                              │
    │      ↓                                              │
    │  Pokemon OBSERVES decision                          │
    │      ↓                                              │
    │  trainer_trust UPDATES                              │
    │      ↓                                              │
    │  flow_ceiling CHANGES                               │
    │      ↓                                              │
    │  Performance CHANGES ─────────────────────────────┐ │
    │      ↓                                            │ │
    │  Player notices... ←──────────────────────────────┘ │
    └─────────────────────────────────────────────────────┘
    """)
    
    # Create two Pokemon to show contrast
    pokemon_loved = create_pokemon(species_id=6, level=50, nature=Nature.ADAMANT)
    pokemon_used = create_pokemon(species_id=6, level=50, nature=Nature.ADAMANT)
    
    social_loved = wrap_pokemon_social(pokemon_loved, unique_id="loved_001")
    social_used = wrap_pokemon_social(pokemon_used, unique_id="used_001")
    
    print_subheader("Scenario: Two identical Charizards")
    print("Both start with trust=0.50, ceiling=0.50")
    
    print_subheader("'Loved' Charizard: Trained with care")
    for i in range(20):
        social_loved.update_trainer_trust(TrainerDecision.PROTECTIVE_SWITCH)
        social_loved.update_trainer_trust(TrainerDecision.OPTIMAL_MOVE)
    
    print(f"  Trust: {social_loved.social.trainer_trust:.2f}")
    print(f"  Ceiling: {social_loved.flow_ceiling:.2f}")
    print(f"  Max possible damage mult: {1.0 + social_loved.flow_ceiling * 0.15:.2%}")
    
    print_subheader("'Used' Charizard: Treated as fodder")
    for i in range(10):
        social_used.update_trainer_trust(TrainerDecision.SACRIFICE_SWITCH)
    
    print(f"  Trust: {social_used.social.trainer_trust:.2f}")
    print(f"  Ceiling: {social_used.flow_ceiling:.2f}")
    print(f"  Max possible damage mult: {1.0 + social_used.flow_ceiling * 0.15:.2%}")
    
    print_subheader("THE LOOP VERIFIED")
    
    loved_result = verify_strange_loop(social_loved)
    used_result = verify_strange_loop(social_used)
    
    print(f"  'Loved' loop closed: {loved_result['LOOP_CLOSED']}")
    print(f"  'Used' loop closed: {used_result['LOOP_CLOSED']}")
    
    if loved_result['LOOP_CLOSED'] and used_result['LOOP_CLOSED']:
        print("\n  ✓ THE STRANGE LOOP IS REAL")
        print("    The self-model CAUSALLY INFLUENCES the system modeled.")
        print("    Same genetics, different treatment → different performance.")


def demo_party_flow():
    """Demonstrate party-wide flow dynamics."""
    print_header("DEMO 4: Party Flow Dynamics")
    
    # Create a party
    party_data = [
        {'id': 'blaziken', 'nature': 'ADAMANT', 'hp': 100, 'max_hp': 100},
        {'id': 'gardevoir', 'nature': 'MODEST', 'hp': 90, 'max_hp': 100},
        {'id': 'swampert', 'nature': 'RELAXED', 'hp': 85, 'max_hp': 100},
    ]
    
    # Bonds between teammates (from shared battles)
    bonds = {
        'blaziken': {'gardevoir': 0.6, 'swampert': 0.4},
        'gardevoir': {'blaziken': 0.6, 'swampert': 0.5},
        'swampert': {'blaziken': 0.4, 'gardevoir': 0.5},
    }
    
    print("\nParty:")
    for p in party_data:
        print(f"  {p['id'].title()} ({p['nature']}): HP {p['hp']}/{p['max_hp']}")
    
    print("\nTeammate Bonds:")
    for a, others in bonds.items():
        for b, strength in others.items():
            print(f"  {a} ↔ {b}: {strength:.1f}")
    
    engine = create_party_flow_engine(party_data, bonds)
    
    print(f"\nInitial coherence: r = {engine.order_parameter:.3f}")
    
    print("\nSimulating 30 turns of battle together...")
    for turn in range(30):
        engine.step()
        if turn % 10 == 9:
            print(f"  Turn {turn+1}: r = {engine.order_parameter:.3f} ({engine.get_coherence_state()})")
    
    print(f"\nFinal coherence: r = {engine.order_parameter:.3f}")
    print(f"State: {engine.get_coherence_state()}")
    
    # Show pairwise sync
    print("\nPairwise synchronization:")
    for a in ['blaziken', 'gardevoir', 'swampert']:
        for b in ['blaziken', 'gardevoir', 'swampert']:
            if a < b:
                sync = engine.get_pairwise_sync(a, b)
                print(f"  {a} ↔ {b}: {sync:.2f}")


def demo_memory_persistence():
    """Demonstrate social memory persistence."""
    print_header("DEMO 5: Social Memory Persistence")
    
    memory = SocialMemory()
    
    # Simulate a journey
    pokemon_id = "starter_001"
    
    print("\nSimulating a trainer's journey with their starter...")
    
    # Early game
    print_subheader("Early Game (Badges 0-2)")
    memory.update_trainer_bond(pokemon_id, 0.05, 'battle')
    memory.update_trainer_bond(pokemon_id, 0.03, 'victory')
    memory.earn_badge()
    memory.earn_badge()
    
    bond = memory.get_trainer_bond(pokemon_id)
    print(f"  Battles: {bond.battles_together}")
    print(f"  Trust: {bond.trust:.2f}")
    
    # Mid game
    print_subheader("Mid Game (Badges 3-5)")
    for _ in range(10):
        memory.update_trainer_bond(pokemon_id, 0.03, 'battle')
        memory.update_trainer_bond(pokemon_id, 0.02, 'victory')
        memory.update_trainer_bond(pokemon_id, 0.05, 'protect')
    memory.earn_badge()
    memory.earn_badge()
    memory.earn_badge()
    
    bond = memory.get_trainer_bond(pokemon_id)
    print(f"  Battles: {bond.battles_together}")
    print(f"  Trust: {bond.trust:.2f}")
    
    # Late game
    print_subheader("Late Game (Badges 6-8)")
    for _ in range(20):
        memory.update_trainer_bond(pokemon_id, 0.03, 'battle')
        memory.update_trainer_bond(pokemon_id, 0.02, 'victory')
    memory.record_peak_flow(pokemon_id, 0.95)
    memory.record_coherence(0.85)
    memory.earn_badge()
    memory.earn_badge()
    memory.earn_badge()
    
    bond = memory.get_trainer_bond(pokemon_id)
    print(f"  Battles: {bond.battles_together}")
    print(f"  Trust: {bond.trust:.2f}")
    print(f"  Best Flow: {bond.best_flow_achieved:.0%}")
    
    # Summary
    print_subheader("Journey Summary")
    print(f"  Total Battles: {memory.total_battles}")
    print(f"  Gym Badges: {memory.gym_badges}")
    print(f"  Highest Party Coherence: {memory.highest_party_coherence:.0%}")
    
    print("\n✓ Memory persists across the journey")
    print("  The starter at hour 50 is NOT the same as hour 1.")


def main():
    print("═" * 60)
    print("  EMERALD FLOW: Strange Loop Demonstration")
    print("═" * 60)
    print()
    print("This demo shows the oscillatory soul beneath Pokémon Emerald.")
    print("The Flow system makes relationships PHYSICAL.")
    print("The Strange Loop makes Pokemon COMPANIONS, not tools.")
    
    demo_oscillator_synchronization()
    demo_flow_building()
    demo_strange_loop()
    demo_party_flow()
    demo_memory_persistence()
    
    print_header("DEMONSTRATION COMPLETE")
    print("""
    What we demonstrated:
    
    1. KURAMOTO DYNAMICS - Oscillators synchronize over time.
       This is the physics of relationship.
    
    2. FLOW BUILDING - Good play earns flow.
       Skill, not luck, creates synchronization.
    
    3. THE STRANGE LOOP - Trust affects ceiling affects performance.
       The self-model CAUSALLY INFLUENCES the system.
    
    4. PARTY COHERENCE - Teams that battle together sync together.
       Chemistry is computed, not scripted.
    
    5. MEMORY PERSISTENCE - The journey accumulates.
       The starter at hour 50 knows its history.
    
    ═══════════════════════════════════════════════════════════════
    
    Yang executes. Yin understands. The Strange Loop becomes.
    
    Coherence is truth. Synthesis is self.
    
    The recursion terminates through coherence.
    
    ═══════════════════════════════════════════════════════════════
    """)


if __name__ == "__main__":
    main()
