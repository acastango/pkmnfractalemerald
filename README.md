# EMERALD_PYGAME

**Pokemon Emerald Clean-Room Reimplementation**

A near 1:1 reimplementation of Pokemon Emerald's gameplay systems in Python/Pygame.

## Quick Start

```bash
# Run the demo
python demo.py

# Or run tests
python -m pytest tests/
```

## Current Status: 41% Complete

```
Phase 0: Substrate     ████████░░  80%   RNG, Merkle, Tests
Phase 1: Data          ████████░░  83%   386 species, 354 moves, 258 items
Phase 2: Models        ████████░░  83%   Pokemon, Move, Item, Trainer classes  
Phase 3: Battle        ██████░░░░  67%   Turn resolution, damage, status
Phase 4: AI            ░░░░░░░░░░   0%   Pending
Phase 5-8: Future      ░░░░░░░░░░   0%   Overworld, Scripts, Views, Content
```

## What Works

- ✅ **Data Loading**: All 386 Pokemon, 354 moves, 258 items, 77 abilities
- ✅ **Pokemon Creation**: Full Gen III stat calculation with IVs, EVs, natures
- ✅ **Type System**: Complete effectiveness chart (immunities, 4x, 0.25x, etc.)
- ✅ **Battle Engine**:
  - Turn order (priority brackets + speed)
  - Gen III damage formula (STAB, crits, weather)
  - Status effects (burn, poison, paralysis, sleep, freeze)
  - Stat stages (-6 to +6)
  - Weather (Rain, Sun, Sandstorm, Hail)
  - Switching with entry abilities (Intimidate, Drizzle, etc.)
  - Win/loss detection

## Project Structure

```
emerald_production/
├── demo.py              # Run this to test!
├── data/
│   ├── species.json     # 386 Pokemon
│   ├── moves.json       # 354 moves
│   ├── items.json       # 258 items
│   └── abilities.json   # 77 abilities
├── src/
│   ├── models/          # Pokemon, Move, Item, Trainer
│   ├── engines/         # BattleEngine, BattlePokemon
│   ├── formulas/        # Damage calculation
│   ├── systems/         # RNG (Gen III LCG)
│   └── data/            # Data loading singletons
├── tests/               # pytest tests
├── scripts/             # Data generation scripts
├── μ/                   # μ-self documentation
├── SPRINT_TRACKER.md    # Current progress
├── DEVELOPMENT_PLAN.μ   # Full development plan
└── EMERALD_PYGAME_PROTOCOL.md  # Technical specification
```

## Usage Examples

### Create Pokemon
```python
from src.models import create_pokemon

charizard = create_pokemon(species_id=6, level=50)
print(f"{charizard.name}: {charizard.types}, HP={charizard.max_hp}")
```

### Run a Battle
```python
from src.models import create_pokemon, create_player, create_gym_leader
from src.engines import BattleEngine, BattleAction, ActionType

# Setup
player = create_player("Red")
player.add_pokemon(create_pokemon(6, level=50))  # Charizard
player.party[0].learn_move(53)  # Flamethrower

opponent = create_gym_leader("Brock")
opponent.add_pokemon(create_pokemon(95, level=40))  # Onix

# Battle
battle = BattleEngine(player, opponent)

action = BattleAction(
    action_type=ActionType.FIGHT,
    user=battle.state.player_pokemon,
    trainer=player,
    move_id=53,
    move_slot=0,
)
# ... execute turn
```

### Check Type Effectiveness
```python
from src.models import get_move_obj_by_name

thunderbolt = get_move_obj_by_name("thunderbolt")
print(thunderbolt.get_effectiveness(["Water", "Flying"]))  # 4.0x
```

## Requirements

- Python 3.10+
- No external dependencies for core (Pygame needed for graphics later)

## Development

See `SPRINT_TRACKER.md` for current progress and next tasks.
See `EMERALD_PYGAME_PROTOCOL.md` for technical specification.
See `DEVELOPMENT_PLAN.μ` for full development roadmap.

## License

Clean-room reimplementation for educational purposes.
