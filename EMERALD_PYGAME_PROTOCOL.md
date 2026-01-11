---
merkle: pending
file: EMERALD_PYGAME_PROTOCOL.md
updated: 2026-01-11
version: 1.0.0
---
# POKÉMON EMERALD PYGAME PRODUCTION PROTOCOL

## μ-Selves Cognitive Boot Sequence for Clean-Room Reimplementation

*"The map processes the territory. The code embodies the design."*

---

## 1. PROJECT IDENTITY

**EMERALD_PYGAME** is a near 1:1 clean-room reimplementation of Pokémon Emerald's gameplay systems, rendered through Pygame. It exists to preserve *mechanical truth* while enabling modern architectural freedom. The central insight is that Emerald is a deterministic state machine ensemble—battle engine, overworld engine, script VM—coupled by shared save-state and a seeded RNG. When reasoning about this project, understand that every formula, every table lookup, every AI decision is a *contract* with the original behavior. Deviation is intentional modification, not accident.

This protocol serves as both **technical specification** and **cognitive scaffold**. Drop it into any conversation to re-instantiate the reasoning architecture for this project.

---

## 2. ARCHITECTURAL OVERVIEW

### 2.1 The Emerald Stack (What We're Mirroring)

```
┌─────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ BattleView  │  │ OverworldView│  │  MenuView   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
├─────────────────────────────────────────────────────────────────┤
│                        ENGINE LAYER                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │BattleEngine │  │ MapEngine   │  │ ScriptVM    │              │
│  │ (turns,dmg) │  │ (tiles,warp)│  │(events,flags)│             │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
├─────────────────────────────────────────────────────────────────┤
│                        MODEL LAYER                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Pokemon     │  │ Trainer     │  │ Item        │              │
│  │ (stats,hp)  │  │ (party,ai)  │  │ (effects)   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ Move        │  │ Ability     │  │ Type        │              │
│  │ (power,eff) │  │ (triggers)  │  │ (matchups)  │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
├─────────────────────────────────────────────────────────────────┤
│                        DATA LAYER                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ SaveData    │  │ GameState   │  │ RNG         │              │
│  │ (persist)   │  │ (flags,vars)│  │ (LCG seed)  │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
├─────────────────────────────────────────────────────────────────┤
│                        STATIC DATA                               │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ species.json │ moves.json │ items.json │ trainers.json      ││
│  │ type_chart.json │ abilities.json │ maps/ │ scripts/         ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 The μ-Selves Mapping

| μ-Level | Code Construct | Emerald Concept | Example |
|---------|----------------|-----------------|---------|
| **μ-self** (L1) | Variable | Atomic value | `pokemon.current_hp`, `FLAG_BADGE_01` |
| **μ-complex** (L2) | Line/Expression | Single operation | `damage = (2*level/5+2) * power * atk/def / 50 + 2` |
| **μ-structure** (L3) | Function | Behavior unit | `calculate_damage()`, `apply_status()` |
| **μ-role** (L4) | Class | Identity | `Pokemon`, `BattleEngine`, `TrainerAI` |

---

## 3. μ-ROLE REGISTRY

### 3.1 Pokemon

```python
# μ-role: Pokemon
# Identity: I am a creature of battle—a being with elemental nature that can be hurt and can act.
# Purpose: I exist to be the subject of combat drama. Without me, there is no one to win or lose.
```

**State (μ-selves):**
| μ-self | Type | Range | Meaning |
|--------|------|-------|---------|
| `species_id` | int | 1-386 | My genetic identity |
| `level` | int | 1-100 | My growth tier |
| `current_hp` | int | 0-max_hp | How alive I am right now |
| `max_hp` | int | computed | My vitality ceiling |
| `attack` | int | computed | Physical striking power |
| `defense` | int | computed | Physical resilience |
| `sp_attack` | int | computed | Special striking power |
| `sp_defense` | int | computed | Special resilience |
| `speed` | int | computed | Temporal advantage |
| `ivs` | int[6] | 0-31 each | Hidden genetic potential |
| `evs` | int[6] | 0-255 each, sum ≤510 | Accumulated training effort |
| `nature` | str | 25 options | Personality modifier (±10% to stats) |
| `ability` | str | species-defined | Passive power |
| `status` | enum | None/PSN/BRN/PAR/SLP/FRZ | Major affliction |
| `moveset` | Move[4] | species-limited | What I can do |
| `held_item` | Item? | any holdable | What I carry |
| `friendship` | int | 0-255 | Bond with trainer |
| `experience` | int | growth-curve | Progress to next level |

**Behaviors (μ-structures):**
- `compute_stat(stat_name) -> int`: Gen III formula with IV/EV/nature
- `take_damage(amount) -> int`: Reduce HP, return actual damage taken
- `apply_status(status) -> bool`: Apply condition if valid
- `use_move(move, target) -> MoveResult`: Execute action
- `gain_experience(amount) -> list[LevelUpEvent]`: Add EXP, handle level-ups
- `check_evolution() -> Species?`: Return evolution target if conditions met
- `can_fight() -> bool`: HP > 0 and not fully incapacitated

**Coherence Anchors:**
1. `current_hp ∈ [0, max_hp]` — Cannot be more alive than maximum
2. `sum(evs) ≤ 510` — Training has limits
3. `len(moveset) ≤ 4` — Move slots are finite
4. Stat formulas MUST match Gen III exactly

---

### 3.2 Move

```python
# μ-role: Move
# Identity: I am an intention crystallized into action—type, power, and consequence.
# Purpose: I exist to transform will into effect. Without me, battles are stalemates.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `move_id` | int | Unique identifier (1-354) |
| `name` | str | Human-readable name |
| `type` | Type | Elemental nature |
| `category` | enum | Physical/Special/Status (Gen III: type-based) |
| `power` | int? | Base damage (null for status moves) |
| `accuracy` | int? | Hit chance (null = always hits) |
| `pp` | int | Uses per healing cycle |
| `priority` | int | Turn order modifier (-7 to +7) |
| `effect_id` | str | Behavioral contract (what special effects) |
| `flags` | set | Contact, Sound, Protect-blocked, etc. |

**Gen III Category Rule:**
```python
PHYSICAL_TYPES = {'Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 
                  'Rock', 'Bug', 'Ghost', 'Steel'}
SPECIAL_TYPES = {'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 
                 'Ice', 'Dragon', 'Dark'}
# Category is determined by move TYPE, not move itself
```

---

### 3.3 BattleEngine

```python
# μ-role: BattleEngine
# Identity: I am the arena where intentions collide under fixed rules.
# Purpose: I exist to execute Gen III battle rules exactly and transparently.
#          Without me, moves are descriptions with no consequences.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `battle_type` | enum | Single/Double/Wild/Trainer |
| `participants` | list[BattlePokemon] | Active combatants + benches |
| `weather` | enum | None/Rain/Sun/Sandstorm/Hail |
| `weather_turns` | int | Remaining weather duration |
| `field_effects` | dict | Reflect, Light Screen, Spikes, etc. |
| `turn_count` | int | How many turns have passed |
| `action_queue` | list[Action] | Actions to resolve this turn |
| `rng` | RNG | Randomness source |
| `log` | list[BattleEvent] | Audit trail for replay |

**Behaviors (μ-structures):**

#### `begin_battle(player_party, opponent_party, battle_type) -> BattleState`
Initialize all battle state. Lead Pokemon enter field. Trigger entry abilities (Intimidate, Drizzle, etc.).

#### `queue_action(participant_id, action) -> bool`
Validate and stage an action (Attack, Switch, Item, Run).

#### `resolve_turn() -> list[BattleEvent]`
**THE CORE μ-STRUCTURE.** Executes one full turn:

```
1. Sort actions by priority tier:
   - Switching/Items: priority +6 (before all moves)
   - Moves: by move.priority, then speed, then random tiebreak
   
2. For each action in order:
   a. Check if actor still able to act (not fainted, not flinched)
   b. If Attack:
      - Check accuracy
      - Calculate damage (see damage formula)
      - Apply damage
      - Apply secondary effects
      - Check for fainting
   c. If Switch: Execute switch, trigger entry effects
   d. If Item: Apply item effect
   
3. End-of-turn effects:
   - Weather damage (Sandstorm, Hail)
   - Status damage (Burn, Poison, Toxic counter)
   - Held item effects (Leftovers, Black Sludge)
   - Ability triggers (Speed Boost, etc.)
   
4. Check win/loss conditions
```

#### `calculate_damage(attacker, move, defender) -> int`
**THE DAMAGE FORMULA (Gen III):**

```python
def calculate_damage(attacker, move, defender, battle_state):
    # Base damage calculation
    level = attacker.level
    power = get_effective_power(move, attacker, defender, battle_state)
    
    # Determine attack/defense stats based on move category
    if move.type in PHYSICAL_TYPES:
        attack = get_effective_stat(attacker, 'attack', battle_state)
        defense = get_effective_stat(defender, 'defense', battle_state)
    else:
        attack = get_effective_stat(attacker, 'sp_attack', battle_state)
        defense = get_effective_stat(defender, 'sp_defense', battle_state)
    
    # Core formula
    damage = ((2 * level / 5 + 2) * power * attack / defense) / 50 + 2
    
    # Modifier chain (multiplicative)
    modifiers = 1.0
    
    # Weather modifier
    modifiers *= get_weather_modifier(move.type, battle_state.weather)
    
    # Critical hit (2x in Gen III, ignores stat stages)
    is_crit, crit_mult = check_critical(attacker, move)
    modifiers *= crit_mult
    
    # STAB (Same Type Attack Bonus)
    if move.type in attacker.types:
        modifiers *= 1.5
    
    # Type effectiveness
    effectiveness = get_type_effectiveness(move.type, defender.types)
    modifiers *= effectiveness
    
    # Burn penalty (physical moves only, 0.5x)
    if attacker.status == 'BRN' and move.type in PHYSICAL_TYPES:
        modifiers *= 0.5
    
    # Random factor (85-100%)
    random_factor = rng.randint(85, 100) / 100
    modifiers *= random_factor
    
    # Apply all modifiers
    final_damage = int(damage * modifiers)
    
    # Minimum 1 damage if not immune
    if effectiveness > 0 and final_damage < 1:
        final_damage = 1
    
    return final_damage
```

---

### 3.4 TrainerAI

```python
# μ-role: TrainerAI
# Identity: I am the decision-maker behind the opponent's strategy.
# Purpose: I exist to simulate intelligent opposition without cheating.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `ai_flags` | set | Which behaviors are enabled |
| `item_count` | dict | Remaining items to use |
| `difficulty` | int | 0-7, affects decision quality |

**AI Flag System (from decomp):**
```python
AI_FLAG_CHECK_BAD_MOVE     = 0x001  # Avoid moves that will fail
AI_FLAG_TRY_TO_FAINT       = 0x002  # Prioritize KO moves
AI_FLAG_CHECK_VIABILITY    = 0x004  # Score moves by effectiveness
AI_FLAG_SETUP_FIRST_TURN   = 0x008  # Consider stat-boosting
AI_FLAG_RISKY              = 0x010  # Take calculated risks
AI_FLAG_PREFER_STRONGEST   = 0x020  # Favor high-power moves
AI_FLAG_PREFER_BATON_PASS  = 0x040  # Baton Pass logic
AI_FLAG_DOUBLE_BATTLE      = 0x080  # Multi-target awareness
AI_FLAG_HP_AWARE           = 0x100  # Use items when low HP
AI_FLAG_SMART_SWITCHING    = 0x200  # Type-matchup switching
```

**Behaviors (μ-structures):**

#### `choose_action(battle_state, my_pokemon) -> Action`
```python
def choose_action(self, state, pokemon):
    # Priority 1: Use healing item if HP critical and items available
    if self.ai_flags & AI_FLAG_HP_AWARE:
        if pokemon.current_hp < pokemon.max_hp * 0.25:
            item = self.get_healing_item()
            if item:
                return Action.UseItem(item, pokemon)
    
    # Priority 2: Switch if terrible matchup and switching enabled
    if self.ai_flags & AI_FLAG_SMART_SWITCHING:
        if should_switch(state, pokemon, self.party):
            return Action.Switch(best_switch_target())
    
    # Priority 3: Score all moves and pick best
    move_scores = []
    for move in pokemon.moveset:
        if move.current_pp <= 0:
            continue
        score = self.score_move(state, pokemon, move)
        move_scores.append((move, score))
    
    if not move_scores:
        return Action.Struggle()
    
    # Higher difficulty = more deterministic choice
    # Lower difficulty = more random selection
    return self.select_move_by_score(move_scores)
```

#### `score_move(state, attacker, move) -> int`
```python
def score_move(self, state, attacker, move):
    score = 100  # Base score
    
    target = state.get_opponent_lead()
    
    # Type effectiveness bonus
    eff = get_type_effectiveness(move.type, target.types)
    if eff >= 2.0:
        score += 40
    elif eff > 1.0:
        score += 20
    elif eff < 1.0 and eff > 0:
        score -= 20
    elif eff == 0:
        score -= 100  # Immune
    
    # Power bonus
    if move.power:
        score += move.power // 10
    
    # Accuracy penalty
    if move.accuracy and move.accuracy < 100:
        score -= (100 - move.accuracy) // 2
    
    # STAB bonus
    if move.type in attacker.types:
        score += 15
    
    # Check if this move would KO
    if self.ai_flags & AI_FLAG_TRY_TO_FAINT:
        estimated_damage = estimate_damage(attacker, move, target)
        if estimated_damage >= target.current_hp:
            score += 50
    
    return score
```

---

### 3.5 MapEngine

```python
# μ-role: MapEngine
# Identity: I am the space where the player exists and moves between battles.
# Purpose: I exist to render Hoenn and handle tile-based movement and warps.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `current_map_id` | int | Which map is loaded |
| `player_x` | int | Tile X coordinate |
| `player_y` | int | Tile Y coordinate |
| `facing` | enum | N/S/E/W |
| `map_data` | MapData | Tiles, events, warps |
| `npcs` | list[NPC] | Active NPCs on this map |
| `encounter_rate` | int | Wild encounter probability |

**Behaviors (μ-structures):**
- `load_map(map_id)`: Initialize map state
- `move_player(direction) -> MoveResult`: Handle collision, warps, encounters
- `check_wild_encounter() -> Pokemon?`: RNG-based encounter spawning
- `interact(direction) -> Event?`: Talk to NPC, read sign, etc.
- `warp_to(map_id, x, y)`: Transition to new map

---

### 3.6 ScriptVM

```python
# μ-role: ScriptVM
# Identity: I am the narrator—the executor of story events and NPC behaviors.
# Purpose: I exist to run event scripts that modify game state.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `script_stack` | list[ScriptContext] | Active script execution |
| `flags` | bool[0x300] | 768 event flags |
| `vars` | int[0x100] | 256 script variables |
| `text_box_active` | bool | Is dialogue showing? |

**Script Commands (partial):**
```python
SCRIPT_COMMANDS = {
    'msgbox': display_text,
    'setflag': lambda flag_id: flags[flag_id] = True,
    'clearflag': lambda flag_id: flags[flag_id] = False,
    'checkflag': lambda flag_id: vars['RESULT'] = flags[flag_id],
    'setvar': lambda var_id, value: vars[var_id] = value,
    'giveitem': lambda item_id, count: add_to_bag(item_id, count),
    'givepokemon': lambda species, level: add_to_party(species, level),
    'wildbattle': lambda species, level: start_wild_battle(species, level),
    'trainerbattle': lambda trainer_id: start_trainer_battle(trainer_id),
    'warp': lambda map_id, x, y: map_engine.warp_to(map_id, x, y),
    'fadescreen': lambda mode: presentation.fade(mode),
    'playbgm': lambda track_id: audio.play_music(track_id),
    # ... 100+ more commands
}
```

---

### 3.7 GameState

```python
# μ-role: GameState
# Identity: I am the persistent memory—everything the game needs to remember.
# Purpose: I exist to be saved, loaded, and modified across sessions.
```

**State (μ-selves):**
| μ-self | Type | Meaning |
|--------|------|---------|
| `player_name` | str | Max 7 chars |
| `player_gender` | enum | Male/Female |
| `trainer_id` | int | 16-bit public ID |
| `secret_id` | int | 16-bit hidden ID |
| `party` | Pokemon[6] | Current team |
| `pc_boxes` | Pokemon[14][30] | PC storage |
| `bag` | dict[pocket -> list[(item, count)]] | Inventory |
| `money` | int | 0 to 999,999 |
| `badges` | bool[8] | Gym progress |
| `flags` | bool[0x300] | Event flags |
| `vars` | int[0x100] | Script variables |
| `play_time` | int | Frames elapsed |
| `pokedex_seen` | set[int] | Species observed |
| `pokedex_caught` | set[int] | Species captured |

---

### 3.8 RNG

```python
# μ-role: RNG
# Identity: I am the source of controlled chaos—deterministic randomness.
# Purpose: I exist to make battles unpredictable yet reproducible.
```

**The Gen III Linear Congruential Generator:**
```python
class Gen3RNG:
    def __init__(self, seed: int):
        self.state = seed & 0xFFFFFFFF
    
    def next(self) -> int:
        # Gen III LCG: state = (state * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
        self.state = (self.state * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
        return self.state >> 16  # Return high 16 bits
    
    def randint(self, lo: int, hi: int) -> int:
        return lo + (self.next() % (hi - lo + 1))
    
    def check(self, threshold: int) -> bool:
        """Return True if next() < threshold (for accuracy/effect checks)"""
        return self.next() < threshold
```

---

## 4. μ-COMPLEX CATALOG (Critical Operations)

### 4.1 Stat Calculation (Gen III Formula)

```python
# μ-complex: compute_stat
# μ-selves involved: base_stat, iv, ev, level, nature

def compute_stat(pokemon, stat_name):
    base = SPECIES_DATA[pokemon.species_id].base_stats[stat_name]
    iv = pokemon.ivs[stat_name]
    ev = pokemon.evs[stat_name]
    level = pokemon.level
    
    if stat_name == 'hp':
        # HP formula: ((2*Base + IV + EV/4) * Level / 100) + Level + 10
        stat = ((2 * base + iv + ev // 4) * level // 100) + level + 10
    else:
        # Other stats: ((2*Base + IV + EV/4) * Level / 100) + 5) * Nature
        stat = ((2 * base + iv + ev // 4) * level // 100) + 5
        stat = int(stat * get_nature_modifier(pokemon.nature, stat_name))
    
    return stat
```

### 4.2 Type Effectiveness Lookup

```python
# μ-complex: type_effectiveness
# μ-selves involved: move_type, defender_types

TYPE_CHART = {
    # (attack_type, defend_type) -> multiplier
    ('Fire', 'Grass'): 2.0,
    ('Fire', 'Water'): 0.5,
    ('Fire', 'Fire'): 0.5,
    ('Water', 'Fire'): 2.0,
    ('Water', 'Grass'): 0.5,
    ('Electric', 'Water'): 2.0,
    ('Electric', 'Ground'): 0.0,  # Immunity
    ('Ground', 'Electric'): 2.0,
    ('Ground', 'Flying'): 0.0,    # Immunity
    # ... 17x17 full matrix
}

def get_type_effectiveness(move_type, defender_types):
    multiplier = 1.0
    for def_type in defender_types:
        mult = TYPE_CHART.get((move_type, def_type), 1.0)
        multiplier *= mult
    return multiplier
```

### 4.3 Experience Formula (Gen III)

```python
# μ-complex: experience_gain
# μ-selves involved: base_exp, enemy_level, is_trainer, has_lucky_egg, is_traded

def calculate_experience(fainted_pokemon, participating, battle_type):
    base = SPECIES_DATA[fainted_pokemon.species_id].exp_yield
    level = fainted_pokemon.level
    
    # Base formula: (Base × Level) / 7
    exp = (base * level) // 7
    
    # Trainer battle bonus (1.5x)
    if battle_type == 'trainer':
        exp = exp * 3 // 2
    
    # Lucky Egg bonus (1.5x)
    if participating.held_item == 'Lucky Egg':
        exp = exp * 3 // 2
    
    # Trade bonus (1.5x for foreign OT)
    if participating.original_trainer != player.trainer_id:
        exp = exp * 3 // 2
    
    # Split among participants
    exp = exp // len(participating)
    
    return exp
```

### 4.4 Accuracy Check

```python
# μ-complex: accuracy_check
# μ-selves involved: move_accuracy, user_accuracy_stage, target_evasion_stage

def check_accuracy(user, move, target, rng):
    if move.accuracy is None:
        return True  # Moves like Swift always hit
    
    # Get stage modifiers
    acc_stage = user.stat_stages['accuracy']
    eva_stage = target.stat_stages['evasion']
    net_stage = max(-6, min(6, acc_stage - eva_stage))
    
    # Stage multipliers (Gen III)
    stage_mult = {
        -6: 33/100, -5: 36/100, -4: 43/100, -3: 50/100,
        -2: 60/100, -1: 75/100,  0: 100/100,
         1: 133/100, 2: 166/100, 3: 200/100,
         4: 233/100, 5: 266/100, 6: 300/100
    }
    
    effective_acc = int(move.accuracy * stage_mult[net_stage])
    return rng.randint(1, 100) <= effective_acc
```

### 4.5 Critical Hit Check

```python
# μ-complex: critical_check
# μ-selves involved: crit_stage, move_high_crit_flag

def check_critical(attacker, move, rng):
    # Base crit rates by stage (Gen III)
    # Stage 0: 1/16, Stage 1: 1/8, Stage 2: 1/4, Stage 3: 1/3, Stage 4+: 1/2
    base_stage = 0
    
    if move.flags.get('high_crit'):
        base_stage += 1
    
    if attacker.held_item == 'Scope Lens':
        base_stage += 1
    
    if attacker.ability == 'Super Luck':
        base_stage += 1
    
    crit_thresholds = {0: 16, 1: 8, 2: 4, 3: 3}
    threshold = crit_thresholds.get(base_stage, 2)
    
    is_crit = rng.randint(1, threshold) == 1
    return is_crit, 2.0 if is_crit else 1.0
```

---

## 5. COHERENCE ANCHORS (Invariants)

These MUST always hold. Violation indicates a bug.

1. **HP is bounded:** `0 ≤ current_hp ≤ max_hp`
2. **EV cap enforced:** `sum(evs) ≤ 510` and `each_ev ≤ 255`
3. **Move slots finite:** `len(moveset) ≤ 4`
4. **PP bounded:** `0 ≤ current_pp ≤ max_pp`
5. **Type effectiveness symmetric per pair:** Fire→Grass is always 2x
6. **Fainted cannot act:** `can_fight() == False` blocks all actions
7. **Damage ≥ 1 if not immune:** Contact means consequence
8. **Status effects persist:** Only cured by specific actions
9. **RNG is deterministic:** Same seed → same sequence
10. **Turn order is deterministic:** Same speeds/priorities/seed → same order

---

## 6. DATA SCHEMA CONTRACTS

### 6.1 Species Data

```json
{
  "species_id": 1,
  "name": "Bulbasaur",
  "types": ["Grass", "Poison"],
  "base_stats": {"hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45},
  "abilities": ["Overgrow"],
  "growth_rate": "medium_slow",
  "catch_rate": 45,
  "exp_yield": 64,
  "gender_ratio": 0.875,
  "egg_groups": ["Monster", "Grass"],
  "evolution": {"method": "level", "level": 16, "into": 2},
  "learnset": {
    "level": {"1": ["Tackle", "Growl"], "7": ["Leech Seed"], "13": ["Vine Whip"]},
    "tm": ["TM06", "TM09", "TM10"],
    "tutor": ["Body Slam"]
  }
}
```

### 6.2 Move Data

```json
{
  "move_id": 85,
  "name": "Flamethrower",
  "type": "Fire",
  "category": "special",
  "power": 90,
  "accuracy": 100,
  "pp": 15,
  "priority": 0,
  "effect_id": "burn_10_percent",
  "flags": ["protect_blocked"],
  "secondary_effects": [{"type": "status", "status": "BRN", "chance": 10}]
}
```

### 6.3 Trainer Data

```json
{
  "trainer_id": 1,
  "name": "Roxanne",
  "class": "Leader",
  "ai_flags": ["CHECK_VIABILITY", "TRY_TO_FAINT", "HP_AWARE"],
  "items": [{"item": "Hyper Potion", "count": 2}],
  "party": [
    {"species": "Geodude", "level": 12, "moves": ["Tackle", "Defense Curl", "Rock Throw"]},
    {"species": "Geodude", "level": 12, "moves": ["Tackle", "Defense Curl", "Rock Throw"]},
    {"species": "Nosepass", "level": 15, "moves": ["Tackle", "Harden", "Rock Throw", "Block"]}
  ]
}
```

---

## 7. MERKLE PROVENANCE SYSTEM

Every source file includes a Merkle header for provenance tracking:

**Python files:**
```python
#!/usr/bin/env python3
# ============================================================================
# MERKLE =====================================================================
# hash: [16-char SHA-256 prefix]
# file: filename.py
# updated: YYYY-MM-DD
# references:
#   species_data.json [hash]
#   moves_data.json [hash]
# END MERKLE =================================================================
# ============================================================================
```

**JSON data files:**
```json
{
  "_merkle": {
    "hash": "[16-char SHA-256 prefix]",
    "file": "species_data.json",
    "updated": "YYYY-MM-DD",
    "source": "Bulbapedia extraction 2026-01-11"
  },
  "data": [...]
}
```

---

## 8. FILE STRUCTURE

```
emerald_pygame/
├── EMERALD_PYGAME_PROTOCOL.md      # This document
├── attach_merkle_headers.py        # Merkle hash utility
├── pyproject.toml                  # Project config
│
├── src/
│   ├── __init__.py
│   ├── main.py                     # Entry point
│   │
│   ├── models/                     # μ-roles (data models)
│   │   ├── pokemon.py              # Pokemon class
│   │   ├── move.py                 # Move class
│   │   ├── item.py                 # Item class
│   │   ├── trainer.py              # Trainer + TrainerAI
│   │   └── types.py                # Type enum + chart
│   │
│   ├── engines/                    # μ-roles (game engines)
│   │   ├── battle_engine.py        # BattleEngine
│   │   ├── map_engine.py           # MapEngine
│   │   ├── script_vm.py            # ScriptVM
│   │   └── encounter_engine.py     # Wild encounter logic
│   │
│   ├── systems/                    # Support systems
│   │   ├── game_state.py           # GameState
│   │   ├── save_system.py          # Save/Load
│   │   ├── rng.py                  # Gen3RNG
│   │   └── audio.py                # Sound management
│   │
│   ├── views/                      # Pygame rendering
│   │   ├── battle_view.py          # Battle screen
│   │   ├── overworld_view.py       # Map screen
│   │   ├── menu_view.py            # Menus
│   │   └── sprites.py              # Sprite management
│   │
│   └── formulas/                   # μ-structures (pure functions)
│       ├── damage.py               # Damage calculation
│       ├── stats.py                # Stat calculation
│       ├── experience.py           # EXP/leveling
│       └── accuracy.py             # Hit/crit checks
│
├── data/
│   ├── species.json                # All 386 Pokemon
│   ├── moves.json                  # All 354 moves
│   ├── items.json                  # All items
│   ├── abilities.json              # All 77 abilities
│   ├── trainers.json               # All trainer data
│   ├── type_chart.json             # 17x17 effectiveness
│   ├── maps/                       # Map data files
│   └── scripts/                    # Event scripts
│
├── μ/                              # μ-selves documentation
│   ├── _index.μ                    # Project manifest
│   ├── battle_system.μ             # Battle μ-role docs
│   ├── pokemon_model.μ             # Pokemon μ-role docs
│   └── ...
│
├── tests/
│   ├── test_damage_formula.py      # Formula verification
│   ├── test_type_chart.py          # Type effectiveness
│   └── test_rng.py                 # RNG sequence verification
│
└── assets/                         # Pygame assets (non-ROM)
    ├── sprites/
    ├── fonts/
    └── sounds/
```

---

## 9. IMPLEMENTATION PHASES

### Phase 1: Core Models (Week 1-2)
- [ ] Pokemon class with stat calculation
- [ ] Move class with all 354 moves loaded
- [ ] Type chart implementation
- [ ] RNG (Gen III LCG)
- [ ] Unit tests for formulas

### Phase 2: Battle Engine (Week 3-4)
- [ ] BattleEngine skeleton
- [ ] Damage calculation (full formula)
- [ ] Accuracy/crit checks
- [ ] Status effects (burn, poison, paralyze, sleep, freeze)
- [ ] Turn order resolution
- [ ] Wild battle flow

### Phase 3: Trainer AI (Week 5)
- [ ] AI flag system
- [ ] Move scoring algorithm
- [ ] Item usage logic
- [ ] Switching logic

### Phase 4: Overworld (Week 6-7)
- [ ] MapEngine with tile collision
- [ ] Player movement
- [ ] NPC placement
- [ ] Wild encounters
- [ ] Warps

### Phase 5: Script VM (Week 8)
- [ ] Basic script interpreter
- [ ] Flag/var system
- [ ] Dialogue display
- [ ] Event triggers

### Phase 6: Pygame Views (Week 9-10)
- [ ] Battle view with animations
- [ ] Overworld tilemap rendering
- [ ] Menu system
- [ ] Sound integration

### Phase 7: Content & Polish (Week 11-12)
- [ ] All trainers implemented
- [ ] Story progression
- [ ] Save/load system
- [ ] Bug fixes and balance verification

---

## 10. USAGE

### Cognitive Boot Sequence

When starting a new conversation:
```
Here's my project's μ-Selves cognitive scaffold:

[paste EMERALD_PYGAME_PROTOCOL.md]

I need to work on [specific area]. The relevant μ-roles are [X] and [Y].
```

### Development Loop

1. Pick a subsystem (Battle, Map, Script)
2. Read the μ-role documentation in this protocol
3. Implement the μ-structures (functions) one at a time
4. Verify against coherence anchors
5. Run Merkle header script to update hashes
6. Commit with clear provenance

### Debugging

When something fails:
1. Identify which μ-structure is misbehaving
2. Check coherence anchors for that μ-role
3. Trace the μ-complex (line) where divergence occurs
4. The bug is where yang (code) ≠ yin (intended behavior)

---

*Yang executes. Yin understands. The answer lives in the space between.*
