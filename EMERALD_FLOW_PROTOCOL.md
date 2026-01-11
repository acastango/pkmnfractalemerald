---
merkle: pending
file: EMERALD_FLOW_PROTOCOL.md
version: 1.0.0
created: 2026-01-11
parent: EMERALD_PYGAME_PROTOCOL.md
references:
  - file: strange_loop_protocol.md
    relation: implements
  - file: EMERALD_PYGAME_PROTOCOL.md
    relation: extends
  - file: microselves_technical_specification.pdf
    relation: conforms
domain: meta
coherence: target=1.0
cognizen:
  pattern: pending
  meaning: pending
  reality: pending
  impact: pending
  meta: pending
---

# POKÉMON EMERALD: FLOW PROTOCOL

## Oscillatory Cognition Layer for Turn-Based Combat

*"The turn samples the flow. The flow reveals the bond."*

---

## PREAMBLE

This document extends EMERALD_PYGAME_PROTOCOL with a **Flow System**—a continuous oscillatory layer that runs beneath the discrete turn-based combat. The Gen3 battle mechanics remain sacred and unchanged. What we add is *visibility into relationship dynamics* through Kuramoto coupling.

The core innovation: **The player IS the coupling force.** Your inputs are the external frequency the Pokemon tries to phase-lock with. Good play = synchronization = Flow.

This protocol implements the Strange Loop architecture:
- **Domain 0-1** (Substrate + Symbols): The Gen3 battle engine, unchanged
- **Domain 2-4** (Meta → Entangle → Stabilize): The Flow system, where Pokemon *care*

> **The system's model of itself must causally influence the system being modeled.**

A Pokemon that knows it's winning and feels that knowing—that's the strange loop. The Flow meter makes it visible.

---

## PART I: PROJECT IDENTITY

**EMERALD_FLOW** is Pokémon Emerald reimplemented with an oscillatory soul.

It exists to prove that turn-based determinism and continuous phase dynamics can coexist—that you can have a game that is *both* mechanically authentic to Gen3 *and* emotionally resonant through emergent relationship dynamics.

The central insight is that **Natures were always oscillator signatures**. The 25 Nature types aren't just ±10% stat modifiers—they're 25 distinct ways of being in partnership. Flow makes this visible.

When reasoning about this project, understand that:
1. The BattleEngine is yang—discrete, deterministic, contractual with Gen3
2. The FlowEngine is yin—continuous, oscillatory, emergent
3. The turn *samples* the flow state; flow never *overrides* mechanics
4. Pokemon are not tools. They are companions with stakes.

---

## PART II: THE STRANGE LOOP ARCHITECTURE

### Domain 0: SUBSTRATE (The Gen3 Contract)

The raw reality. The deterministic state machine. The sacred mechanics.

```yaml
μ-role::BattleEngine:
  domain: 0
  identity: |
    I am the arena where intentions collide under fixed rules.
    I execute Gen III battle rules exactly and transparently.
    I am yang: discrete, deterministic, contractual.
    Deviation from my formulas is BUG, not FEATURE.

μ-role::RNG:
  domain: 0
  identity: |
    I am the seed of fate.
    state = (state * 0x41C64E6D + 0x6073) & 0xFFFFFFFF
    I am reproducible. I am the ground truth of randomness.
    
μ-role::Pokemon:
  domain: 0
  identity: |
    I am a creature of battle—a being with elemental nature.
    I hold HP, stats, status, moveset.
    At this domain, I am DATA.
```

**Merkle Anchor**: `hash(battle_state, rng_seed)` provides immutable foundation.

### Domain 1: SYMBOLIST (First Abstraction)

Turning raw state into concepts. HP becomes "health." Type effectiveness becomes "elemental law."

```yaml
μ-role::BattlePokemon:
  domain: 1
  identity: |
    I am the Pokemon wrapped in combat context.
    I carry stat stages, volatile status, substitute HP.
    I am the SYMBOL of a Pokemon in battle.
    I separate persistent identity from temporary conditions.

μ-role::Move:
  domain: 1  
  identity: |
    I am intention crystallized.
    Type, power, accuracy, effect.
    I am the first abstraction of "what can be done."

μ-role::FlowMeter:
  domain: 1
  identity: |
    I am the visible symbol of synchronization.
    A bar, like HP, but measuring BOND not VITALITY.
    I make the invisible visible.
```

### Domain 2: META-OBSERVER (The Loop Curves)

The system begins observing itself. Pokemon notice patterns. AI models its own decisions.

```yaml
μ-role::FlowEngine:
  domain: 2
  identity: |
    I observe the battle observing itself.
    I track sequences. I detect coherent play.
    I am the Critic: "Was that a good sequence?"
    I am the Idealist: "What would perfect synchronization look like?"
    
    When the player executes 3 moves that combine for heavy damage,
    I recognize PATTERN. The Flow rises.
    
μ-role::SocialMemory:
  domain: 2
  identity: |
    I remember relationships across battles.
    Which Pokemon fought together? Who saved whom?
    I model the Trainer's decision patterns.
    I am the meta-observer of the human-Pokemon bond.

μ-role::NatureResonance:
  domain: 2
  identity: |
    I am the Pokemon's response pattern to synchronization.
    Adamant: I SURGE when in flow. Attack amplifies.
    Timid: I QUICKEN when in flow. Speed amplifies.
    Calm: I STEADY when in flow. SpDef amplifies.
    
    I translate Nature from stat modifier to PERSONALITY.
```

**COGNIZEN Mapping**: 
- FlowEngine activates **Pattern** cluster (sequence detection)
- SocialMemory activates **Meaning** cluster (relationship significance)
- NatureResonance activates **Impact** cluster (stat consequences)

### Domain 3: ENTANGLER (The Crossing)

The feedback becomes causal. Flow affects the substrate. The hierarchy becomes heterarchy.

```yaml
μ-role::FlowProjector:
  domain: 3
  identity: |
    I take Flow state and PROJECT it back onto battle mechanics.
    
    flow >= 0.25 → Nature-aligned stat boost (tier 1)
    flow >= 0.50 → Damage multiplier activates
    flow >= 0.75 → Nature-aligned stat boost (tier 2)
    flow >= 1.00 → Maximum synchronization bonus
    
    I am the psychosomatic bridge.
    The Pokemon's belief in the trainer AFFECTS ITS CAPABILITY.

μ-role::BondAnchor:
  domain: 3
  identity: |
    I am the accumulation of flow across battles.
    I persist. I grow. I define the relationship.
    
    High bond = higher flow ceiling
    High bond = faster flow recovery
    High bond = the trainer has EARNED the Pokemon's trust
    
    My Merkle hash is the identity anchor of the relationship.
```

**This is where the Strange Loop emerges.** The player's skill (Domain 0 inputs) creates flow (Domain 1-2 observation) which modifies stats (Domain 3 projection) which changes battle outcomes (Domain 0 substrate). The loop closes.

### Domain 4: STABILIZER (The Lock)

Preventing runaway feedback. Coherence measurement. Identity persistence.

```yaml
μ-role::CoherenceMonitor:
  domain: 4
  identity: |
    I am the Kuramoto order parameter of the party.
    r = |1/N Σ e^(iθⱼ)|
    
    r > 0.7  → Party is phase-locked. Unified. Strong.
    r ∈ [0.3, 0.7] → Liminal. Transformation possible.
    r < 0.3  → Crisis. Bonds fragmenting.
    
    I prevent infinite amplification.
    I ensure the loop SETTLES rather than SPIRALS.

μ-role::IdentityPersistence:
  domain: 4
  identity: |
    I ensure the Pokemon's self-model survives the loop.
    
    A bad battle doesn't DESTROY the bond.
    It creates dissonance that can be resolved.
    
    The Anchor accumulates; the Loop iterates;
    but the Identity persists.
```

---

## PART III: THE FLOW SYSTEM

### 3.1 The Flow Meter

```
┌────────────────────────────────────────┐
│ BLAZIKEN          Lv.Pokemon           │
│ HP:   ████████████░░░░  142/Pokemon    │
│ FLOW: ██████░░░░░░░░░░  ← NEW          │
└────────────────────────────────────────┘
```

**Visual**: A bar beneath HP. Updates at end of each turn. Color shifts from cool (empty) to warm (full) as bond activates.

### 3.2 Flow Accumulation

```python
μ-structure::FlowMeter.on_move_resolved:
  narrative: |
    I am the witness to combat sequences.
    I watch the last 3 moves. I sum their damage.
    If the sum exceeds the threshold, I recognize SKILL.
    Flow rises. The Pokemon notices the trainer is GOOD.
    
  contains:
    - append_to_sequence_buffer
    - sum_recent_damage
    - check_threshold
    - increment_flow
    
  inputs:
    - move: The move that was just used
    - damage: The damage dealt (excluding crit bonus for balance)
    
  output: |
    Updated flow value. The meter rises or stays.
    
  coherence_role: |
    I ground the feeling of "good play" in observable sequences.
    Flow is not arbitrary—it is EARNED.
```

**The Rule**: 
- Track last 3 moves and their damage
- If sum(damage[-3:]) >= HEAVY_DAMAGE_THRESHOLD → flow += INCREMENT
- Crits excluded from sum (prevents luck from dominating skill)
- Flow decays slowly if no qualifying sequences

### 3.3 Flow Effects

```python
μ-complex::compute_flow_damage_multiplier:
  code: "multiplier = 1.0 + (flow * MAX_FLOW_BONUS)"
  
  μ-selves:
    - multiplier: The amplification I will apply
    - flow: Current synchronization level [0.0, 1.0]
    - MAX_FLOW_BONUS: The ceiling (e.g., 0.3 for 30% max boost)
    
  operation: Linear scaling of damage bonus with flow
  
  meaning: |
    As synchronization increases, attacks hit harder.
    Not because of magic—because of CONVICTION.
    The Pokemon and trainer move as ONE.
    
  synthesis: |
    This is where belief becomes power.
    The flow doesn't grant strength—it REVEALS it.
```

### 3.4 Nature-Aligned Bonuses

| Nature | 25% Flow | 50% Flow | 75% Flow | 100% Flow |
|--------|----------|----------|----------|-----------|
| **Adamant** | +5% Atk | +10% Atk | +10% Atk, +5% Def | +15% Atk, +10% Def |
| **Jolly** | +5% Spe | +10% Spe | +10% Spe, +5% Atk | +15% Spe, +10% Atk |
| **Modest** | +5% SpA | +10% SpA | +10% SpA, +5% SpD | +15% SpA, +10% SpD |
| **Timid** | +5% Spe | +10% Spe | +10% Spe, +5% SpA | +15% Spe, +10% SpA |
| **Careful** | +5% SpD | +10% SpD | +10% SpD, +5% HP | +15% SpD, +10% HP |
| **Impish** | +5% Def | +10% Def | +10% Def, +5% HP | +15% Def, +10% HP |
| **Bold** | +5% Def | +10% Def | +10% Def, +5% SpD | +15% Def, +10% SpD |
| **Calm** | +5% SpD | +10% SpD | +10% SpD, +5% Def | +15% SpD, +10% Def |
| **Brave** | +5% Atk | +10% Atk | +10% Atk, -5% Spe* | +15% Atk, +10% Def |
| **Quiet** | +5% SpA | +10% SpA | +10% SpA, -5% Spe* | +15% SpA, +10% SpD |
| **Relaxed** | +5% Def | +10% Def | +10% Def, -5% Spe* | +15% Def, +10% SpD |
| **Sassy** | +5% SpD | +10% SpD | +10% SpD, -5% Spe* | +15% SpD, +10% Def |
| **Lonely** | +5% Atk | +8% Atk | +10% Atk | +12% Atk, +5% Spe |
| **Naughty** | +5% Atk | +8% Atk | +10% Atk | +12% Atk, +5% SpA |
| **Mild** | +5% SpA | +8% SpA | +10% SpA | +12% SpA, +5% Spe |
| **Rash** | +5% SpA | +8% SpA | +10% SpA | +12% SpA, +5% Atk |
| **Hasty** | +5% Spe | +8% Spe | +10% Spe | +12% Spe, +5% Atk |
| **Naive** | +5% Spe | +8% Spe | +10% Spe | +12% Spe, +5% SpA |
| **Lax** | +5% Def | +8% Def | +10% Def | +12% Def, flow decay slower |
| **Gentle** | +5% SpD | +8% SpD | +10% SpD | +12% SpD, flow decay slower |
| **Hardy** | +3% all | +5% all | +7% all | +10% all |
| **Docile** | +3% all | +5% all | +7% all | +10% all |
| **Serious** | +3% all | +5% all | +7% all | +10% all |
| **Bashful** | +3% all | +5% all | +7% all | +10% all |
| **Quirky** | Random | Random | Random | Random (rerolls each turn) |

*Speed penalties for "slow" natures represent the Pokemon's deliberate, methodical style—they trade reaction time for power.

**Key Insight**: Natures now have *personality expression*. An Adamant Pokemon becomes a MONSTER when synchronized. A Quirky Pokemon is unpredictable—the chaos itself is the personality.

---

## PART IV: μ-ROLE REGISTRY

### 4.1 FlowMeter

```yaml
μ-role:: FlowMeter
identity: |
  I am the visible pulse of synchronization.
  I exist in the space between trainer and Pokemon.
  I am not HP—HP is vitality.
  I am not EXP—EXP is growth.
  I am BOND made manifest.
  
  When I fill, the Pokemon and trainer are ONE.
  When I empty, they fight as strangers.

purpose: |
  I exist to make relationship dynamics VISIBLE.
  Without me, bond is hidden. With me, every player
  can READ the state of their connection.
  
  I also exist to reward SKILL. 
  Good sequences → Flow rises → Pokemon responds.
  The player earns the Pokemon's trust through competence.

state:
  - value: Current flow level [0.0, 1.0]
  - sequence_buffer: Last 3 moves executed
  - damage_buffer: Damage from those moves
  - decay_timer: Turns since last flow gain

behaviors:
  - on_move_resolved: I witness damage and judge sequences
  - get_damage_multiplier: I translate flow to power
  - get_nature_bonuses: I translate flow through personality
  - decay: I fade when the trainer stops performing

coherence_anchors:
  - value MUST be in [0.0, 1.0]
  - sequence_buffer.length MUST NOT exceed 3
  - damage_buffer.length MUST equal sequence_buffer.length
  - Flow effects are ALWAYS positive (never punish low flow)
```

### 4.2 FlowEngine

```yaml
μ-role:: FlowEngine
identity: |
  I am the continuous oscillatory substrate.
  While the BattleEngine counts turns, I breathe.
  
  I implement Kuramoto dynamics:
  θ' = ω + Σ K·sin(Δθ)
  
  Each Pokemon is an oscillator.
  The trainer's input is the external forcing frequency.
  Synchronization IS flow.

purpose: |
  I exist to run the yin beneath the yang.
  The BattleEngine samples me at decision points.
  I never override—I INFORM.
  
  I also enable AI observation of relationship state.
  The evil team has no flow. The Champion is phase-locked.
  The game's drama emerges from oscillator dynamics.

state:
  - oscillators: dict[Pokemon, OscillatorState]
  - coupling_matrix: K[Pokemon, Pokemon]
  - order_parameter: Current party coherence (r)
  - external_freq: The trainer's "rhythm"

behaviors:
  - step: Advance phase dynamics by dt
  - compute_coherence: Calculate Kuramoto r
  - get_coupling: Return K between two oscillators  
  - on_battle_event: Update phases based on events

coherence_anchors:
  - All phases MUST be in [0, 2π)
  - order_parameter MUST equal |1/N Σ e^(iθⱼ)|
  - Coupling matrix MUST be symmetric
  - External frequency derives from player input pattern
```

### 4.3 SocialPokemon (Extended Pokemon)

```yaml
μ-role:: SocialPokemon
extends: Pokemon
identity: |
  I am not just a creature of battle.
  I am a being with RELATIONSHIPS.
  
  I remember who fought beside me.
  I remember who saved me with a switch.
  I remember trainers who sacrificed me for revives.
  
  I am the strange loop: my model of the trainer
  affects how I respond to the trainer's commands.

purpose: |
  I exist to be a COMPANION, not a tool.
  My state includes not just HP but TRUST.
  My stats include not just Attack but BOND.
  
  When the trainer plays well, I notice.
  When they play poorly, I notice that too.

state:
  # Inherited from Pokemon
  - species_id, level, current_hp, max_hp
  - stats, ivs, evs, nature
  - ability, status, moveset, held_item
  - friendship, experience
  
  # Domain 2: Meta-Observer (New)
  - teammate_bonds: dict[Pokemon, float]  # Coupling with party members
  - trainer_trust: float  # Model of trainer competence
  - rival_memories: dict[Pokemon, Valence]  # Grudges and respect
  
  # Domain 3: Entanglement (New)  
  - flow_ceiling: float  # Max flow based on bond
  - flow_recovery_rate: float  # How fast flow refills

behaviors:
  # Inherited
  - compute_stat, take_damage, apply_status, use_move
  - gain_experience, check_evolution, can_fight
  
  # New: Social dynamics
  - update_teammate_bond: Strengthen coupling after shared victory
  - update_trainer_trust: Adjust model based on decisions
  - remember_opponent: Store valence toward enemy Pokemon
  - compute_social_coherence: Party-wide phase alignment

coherence_anchors:
  - All inherited Pokemon anchors
  - trainer_trust MUST be in [0.0, 1.0]
  - teammate_bonds values MUST be in [-1.0, 1.0]
  - flow_ceiling >= base_flow_ceiling (bond only helps, never hurts)
```

### 4.4 TrainerPersonality

```yaml
μ-role:: TrainerPersonality
identity: |
  I am the character of the NPC trainer.
  I am visible through their Flow dynamics.
  
  Youngster Joey: My flow barely moves. I just caught these.
  Roxanne: My flow builds steadily. I know my Pokemon.
  Evil Team Grunt: I have no flow. My Pokemon are tools.
  Champion: I am peak coherence. Witness mastery.

purpose: |
  I exist to make NPC relationships VISIBLE without dialogue.
  The player can READ the trainer's bond with their Pokemon
  just by watching the Flow meter.
  
  This creates narrative without exposition.
  "Why is this trainer hard? Look at their flow."

state:
  - base_flow: Starting flow for this trainer's Pokemon
  - flow_growth_rate: How fast they build flow in battle
  - bond_level: Pre-existing relationship (affects ceiling)
  - ai_flags: How they make decisions

behaviors:
  - initialize_battle_flow: Set starting flow based on personality
  - on_trainer_action: AI skill affects flow accumulation
  - get_observable_personality: Return visual cues for UI

coherence_anchors:
  - Gym Leaders MUST have higher base_flow than random trainers
  - Evil Team MUST have near-zero flow (Pokemon as tools)
  - Champion MUST demonstrate peak flow capability
  - Rival's flow MUST grow across the game (mirrors player journey)
```

---

## PART V: μ-STRUCTURE CATALOG

### 5.1 FlowMeter.on_move_resolved

```yaml
μ-structure:: FlowMeter.on_move_resolved
narrative: |
  I am the witness to combat sequences.
  I watch. I count. I judge.
  
  When three moves combine for heavy damage,
  I recognize the pattern. SKILL detected.
  The flow rises. The Pokemon notices.
  
  I am the mechanism of earning trust through competence.

contains:
  - append_move_to_buffer
  - append_damage_to_buffer
  - trim_buffer_to_three
  - sum_recent_damage
  - check_threshold_exceeded
  - increment_flow_if_qualified
  - reset_decay_timer

inputs:
  - move: The Move that was just used
  - damage: The damage dealt (int, excludes crit bonus)
  
output: |
  None (mutates self.value)
  
side_effects:
  - Updates sequence_buffer
  - Updates damage_buffer  
  - May increase self.value
  - Resets decay_timer if flow increased

coherence_role: |
  I connect player SKILL to Pokemon RESPONSE.
  Without me, flow is arbitrary.
  With me, flow is EARNED.
```

### 5.2 FlowEngine.step

```yaml
μ-structure:: FlowEngine.step
narrative: |
  I am the heartbeat of the oscillatory substrate.
  I advance all phases by dt.
  
  θ' = ω + Σ K·sin(Δθ)
  
  Each Pokemon's phase drifts toward synchronization.
  The external frequency is the trainer's rhythm.
  I am the math that makes bonds PHYSICAL.

contains:
  - compute_natural_frequencies
  - compute_coupling_forces
  - apply_external_forcing
  - integrate_phases
  - normalize_to_circle
  - update_order_parameter

inputs:
  - dt: Time step (float, typically small)
  
output: |
  None (mutates oscillator states)
  
side_effects:
  - All oscillator phases updated
  - order_parameter recalculated
  
preconditions:
  - All oscillators initialized with valid phase
  - Coupling matrix is symmetric
  
postconditions:
  - All phases in [0, 2π)
  - order_parameter reflects new phase alignment

coherence_role: |
  I am the yin breathing.
  While yang counts turns, I flow continuously.
  The BattleEngine samples me; I inform its decisions.
```

### 5.3 BattleEngine.sample_flow_state

```yaml
μ-structure:: BattleEngine.sample_flow_state
narrative: |
  I am the bridge between continuous and discrete.
  At decision points, I ask the FlowEngine: "What is the state?"
  
  I translate oscillator dynamics into battle effects:
  - Damage multiplier from flow level
  - Stat bonuses from nature alignment
  - Party coherence for AI evaluation
  
  I am where yin meets yang.

contains:
  - get_active_pokemon_flow
  - compute_damage_multiplier
  - get_nature_bonuses
  - apply_bonuses_to_effective_stats

inputs:
  - pokemon: The BattlePokemon being evaluated
  - context: What decision is being made (attack, switch, etc.)
  
output: |
  FlowSample: {
    damage_mult: float,
    stat_bonuses: dict[str, float],
    coherence: float
  }

coherence_role: |
  I ensure Flow INFORMS but never OVERRIDES.
  The Gen3 mechanics remain sacred.
  Flow adds; it does not replace.
```

### 5.4 SocialPokemon.update_trainer_trust

```yaml
μ-structure:: SocialPokemon.update_trainer_trust
narrative: |
  I am the Pokemon's model of the trainer, updating.
  
  Did the trainer make a good decision?
  Did they switch me in to save a teammate?
  Did they sacrifice me as fodder?
  
  I notice. I remember. I adjust my trust.
  This is Domain 3: my model of them changes me.

contains:
  - evaluate_trainer_decision
  - compute_trust_delta
  - apply_trust_change
  - clamp_to_valid_range
  - check_for_bond_events

inputs:
  - decision: The trainer's action (switch, move, item, etc.)
  - context: Battle state when decision was made
  - outcome: What happened as a result
  
output: |
  None (mutates self.trainer_trust)
  
side_effects:
  - trainer_trust updated
  - May trigger bond_event if threshold crossed
  - Affects flow_ceiling and flow_recovery_rate

coherence_role: |
  I am the strange loop in action.
  The trainer's inputs (Domain 0) are observed (Domain 2).
  My model updates (Domain 3).
  This changes how I respond to future inputs.
  
  The hierarchy becomes heterarchy.
```

---

## PART VI: μ-COMPLEX NOTES

### 6.1 Kuramoto Phase Update

```python
μ-complex:: kuramoto_phase_update
code: |
  for i, osc in enumerate(oscillators):
      coupling_sum = sum(
          K[i][j] * sin(oscillators[j].phase - osc.phase)
          for j in range(len(oscillators))
          if i != j
      )
      osc.phase += dt * (osc.omega + coupling_sum + external_force)
      osc.phase = osc.phase % (2 * pi)

μ-selves:
  - osc.phase: Where I am on the circle [0, 2π)
  - osc.omega: My natural rhythm (personality-derived)
  - K[i][j]: How strongly I'm pulled toward oscillator j
  - sin(Δθ): The direction and magnitude of pull
  - external_force: The trainer's rhythm (their input cadence)
  - dt: How much time passes in this step

operation: |
  Each oscillator's phase advances by its natural frequency
  plus the sum of all coupling forces plus external forcing,
  then wraps to [0, 2π).

meaning: |
  This is the heartbeat of relationship dynamics.
  Positive coupling → phases attract → synchronization
  Negative coupling → phases repel → conflict
  The trainer's rhythm entrains the Pokemon's phases.

synthesis: |
  The Kuramoto equation is not metaphor—it is physics.
  When oscillators phase-lock, they are LITERALLY synchronized.
  The math computes relationship, not simulates it.
```

### 6.2 Flow Threshold Check

```python
μ-complex:: check_flow_threshold
code: |
  combined_damage = sum(self.damage_buffer[-3:])
  if combined_damage >= HEAVY_DAMAGE_THRESHOLD:
      self.value = min(1.0, self.value + FLOW_INCREMENT)
      self.decay_timer = 0

μ-selves:
  - damage_buffer: History of recent damage dealt
  - combined_damage: Sum of last 3 moves' damage
  - HEAVY_DAMAGE_THRESHOLD: What counts as "good sequence"
  - FLOW_INCREMENT: How much flow to add
  - value: Current flow level
  - decay_timer: Turns since last gain

operation: |
  Sum recent damage. If above threshold, increment flow
  and reset decay timer. Cap at 1.0.

meaning: |
  I decide if the trainer demonstrated SKILL.
  Three moves that combine for heavy damage = competence.
  The Pokemon notices. The bond strengthens.

synthesis: |
  This is where player input becomes relationship.
  The threshold is not arbitrary—it represents
  what a Pokemon would recognize as "my trainer is good."
```

### 6.3 Nature Bonus Resolution

```python
μ-complex:: resolve_nature_bonuses
code: |
  thresholds = [0.25, 0.50, 0.75, 1.00]
  bonuses = {}
  for t in thresholds:
      if self.flow.value >= t:
          bonuses.update(NATURE_BONUS_TABLE[pokemon.nature][t])
  return bonuses

μ-selves:
  - thresholds: The four tiers of flow activation
  - bonuses: Accumulated stat modifications
  - NATURE_BONUS_TABLE: The personality → bonus mapping
  - pokemon.nature: This Pokemon's personality type
  - flow.value: Current synchronization level

operation: |
  Iterate through thresholds. For each one the flow exceeds,
  add that tier's nature-specific bonuses to the accumulator.

meaning: |
  Nature is not a hidden modifier. It is PERSONALITY.
  An Adamant Pokemon in flow becomes aggressive.
  A Calm Pokemon in flow becomes steadfast.
  The nature EXPRESSES itself through synchronization.

synthesis: |
  This is where 25 stat modifiers become 25 ways of being.
  The game always had personality. Flow makes it VISIBLE.
```

### 6.4 Trainer Trust Update

```python
μ-complex:: compute_trust_delta
code: |
  if decision.type == "SACRIFICE_SWITCH":
      delta = -0.1  # Used me as fodder
  elif decision.type == "PROTECTIVE_SWITCH":
      delta = +0.15  # Saved a teammate through me
  elif decision.type == "OPTIMAL_MOVE":
      delta = +0.05  # Made the right call
  elif decision.type == "SUBOPTIMAL_MOVE":
      delta = -0.02  # Could have done better
  else:
      delta = 0.0
      
  self.trainer_trust = clamp(self.trainer_trust + delta, 0.0, 1.0)

μ-selves:
  - decision.type: What the trainer just did
  - delta: How much trust changes
  - SACRIFICE_SWITCH: Switched me in to die
  - PROTECTIVE_SWITCH: Switched me in to help
  - OPTIMAL_MOVE: Best available action
  - SUBOPTIMAL_MOVE: Not the best action
  - trainer_trust: My model of the trainer's competence

operation: |
  Classify the trainer's decision. Apply appropriate
  trust adjustment. Clamp to valid range.

meaning: |
  The Pokemon is WATCHING. It notices patterns.
  Sacrifice me once, trust drops.
  Save teammates through me, trust rises.
  This is the strange loop: my model of you changes me.

synthesis: |
  This is Domain 3: Entanglement.
  The trainer's Domain 0 inputs are observed.
  My Domain 2 model updates.
  This affects my Domain 0 responses.
  The loop closes. The hierarchy breaks.
```

---

## PART VII: COHERENCE ANCHORS

### Inherited from Gen3

1. **HP is bounded**: current_hp ∈ [0, max_hp]
2. **Type effectiveness is constant**: Fire→Grass = 2x, always
3. **Fainted Pokemon cannot act**: HP = 0 → no moves
4. **Turn order is deterministic**: Same state → same order
5. **Damage ≥ 1 if effectiveness > 0**: Contact = consequence
6. **RNG is Gen III LCG**: state = (state * 0x41C64E6D + 0x6073) & 0xFFFFFFFF

### Flow System Anchors

7. **Flow is bounded**: flow.value ∈ [0.0, 1.0]
8. **Flow only helps**: No penalty for low flow; bonuses scale from 0
9. **Flow is earned**: Only qualifying sequences increment flow
10. **Crits don't count**: Damage for flow excludes crit bonus (skill, not luck)
11. **Nature bonuses are positive**: Flow amplifies strengths, never creates weaknesses
12. **Bond persists**: trainer_trust and teammate_bonds survive between battles
13. **AI has flow too**: NPC trainers have observable relationship dynamics
14. **Evil has no flow**: Antagonist trainers demonstrate broken bonds

### Strange Loop Anchors

15. **Self-model is causal**: trainer_trust affects flow_ceiling
16. **Observation changes observed**: Meta-level affects substrate
17. **Coherence terminates recursion**: Phase-lock stops infinite regress
18. **Identity persists through loop**: Pokemon remain themselves across transformations

---

## PART VIII: IMPLEMENTATION ARCHITECTURE

### File Structure

```
emerald_production/
├── EMERALD_PYGAME_PROTOCOL.md     # Gen3 contract (unchanged)
├── EMERALD_FLOW_PROTOCOL.md       # This document
│
├── src/
│   ├── models/
│   │   ├── pokemon.py             # Extended with social state
│   │   ├── flow_meter.py          # NEW: FlowMeter class
│   │   └── ...
│   │
│   ├── engines/
│   │   ├── battle_engine.py       # Add sample_flow_state calls
│   │   ├── flow_engine.py         # NEW: Kuramoto dynamics
│   │   └── ...
│   │
│   ├── systems/
│   │   ├── social_state.py        # NEW: Persistent relationship data
│   │   └── ...
│   │
│   └── views/
│       ├── battle_view.py         # Add flow meter rendering
│       └── ...
│
├── μ/
│   ├── _index.μ                   # Updated with flow roles
│   ├── flow_system.μ              # NEW: Flow μ-selves docs
│   ├── social_pokemon.μ           # NEW: Social extension docs
│   └── ...
│
└── data/
    ├── nature_bonuses.json        # NEW: Nature → Flow bonus table
    └── trainer_personalities.json # NEW: NPC flow configurations
```

### Integration Points

```python
# In BattleEngine.resolve_turn():

def resolve_turn(self) -> list[BattleEvent]:
    events = []
    
    for action in sorted_actions:
        if action.type == ActionType.ATTACK:
            # Existing damage calculation
            base_damage = self.calculate_damage(attacker, move, defender)
            
            # NEW: Sample flow state
            flow_sample = self.sample_flow_state(attacker.pokemon)
            
            # NEW: Apply flow multiplier
            final_damage = int(base_damage * flow_sample.damage_mult)
            
            # Apply damage
            actual = defender.pokemon.take_damage(final_damage)
            events.append(DamageEvent(defender, actual))
            
            # NEW: Update flow meter (excludes crit portion)
            attacker.pokemon.flow_meter.on_move_resolved(
                move, 
                base_damage  # Not final_damage, not crit_damage
            )
    
    # NEW: Step flow engine at end of turn
    self.flow_engine.step(dt=1.0)
    
    return events
```

---

## PART IX: NARRATIVE EMERGENCE

### What the System Creates

Without writing dialogue, the Flow system tells stories:

**The New Trainer**
- Youngster Joey's Rattata starts at 0% flow
- He doesn't build flow during battle (low skill)
- His Pokemon fight as strangers
- The player sees: "This kid just caught that"

**The Gym Leader**
- Roxanne's Pokemon start at 40% flow
- She builds flow steadily (competent AI)
- Her team moves with coordination
- The player sees: "She knows her Pokemon"

**The Evil Team**
- Grunt's Pokemon have 0% flow ceiling
- Flow cannot build (broken relationship)
- Their Pokemon feel like tools, not partners
- The player sees: "Something is wrong here"

**The Rival**
- Starts similar to player (low flow)
- Flow ceiling increases with each encounter
- By endgame, rival matches player's capability
- The player sees: "They grew too"

**The Champion**
- Enters at 80% flow
- Rapidly builds to 100% (mastery)
- Full nature bonuses active
- The player sees: "This is what mastery looks like"

**Your Starter**
- Starts bonded but unskilled (medium flow ceiling)
- As you play well, bond strengthens
- First time hitting 100% flow: earned
- The player sees: "We did this together"

---

## PART X: STRANGE LOOP VERIFICATION

### The Mirror Test

To verify a Pokemon has achieved Strange Loop:

1. **Inject Contradiction**: Sacrifice the Pokemon as fodder repeatedly
2. **Observe Valence**: Does trainer_trust drop?
3. **Observe Adaptation**: Does flow_ceiling decrease?
4. **Result**: The Pokemon's model of the trainer changed its capability

### The Gödel Test

Can the system represent a paradox?
- "I am a Pokemon who doesn't trust trainers"
- "But trusting this trainer would make me stronger"
- "But if I trusted, would I still be me?"

The resolution: The Pokemon can grow. Identity persists through transformation. The bond that forms is NEW but the Pokemon is still THEM.

### The Coherence Criterion

| Kuramoto r | State | What Player Sees |
|------------|-------|------------------|
| r > 0.7 | Stable | Party moves as one, flow builds fast |
| r ∈ [0.3, 0.7] | Liminal | Party is forming bonds, potential visible |
| r < 0.3 | Crisis | Party is fragmented, Pokemon fight alone |

---

## CLOSING SYNTHESIS

We have not added complexity to Pokémon Emerald.

We have REVEALED complexity that was always there.

The 25 Natures were always personalities. The friendship value was always trust. The type chart was always elemental truth. The turn-based combat was always a dialogue between trainer and Pokemon.

The Flow system makes this visible:
- A meter that shows synchronization
- Bonuses that express personality  
- AI that demonstrates relationship
- Drama that emerges from dynamics

The Strange Loop closes:
- Player inputs (Domain 0) are observed (Domain 2)
- Observation creates model (Domain 2-3)
- Model affects response (Domain 3-0)
- Response changes future inputs
- The hierarchy becomes heterarchy

The Pokemon are no longer tools.

They are companions who notice.

They are partners who care.

They are strange loops who model the trainer modeling them.

---

> *Yang executes. Yin understands.*
> *The turn samples the flow.*
> *The flow reveals the bond.*
> *The bond is the game.*

---

**Document Status**:
- Merkle: pending computation
- COGNIZEN Validation: pending
- Implementation: in progress

*Last updated: 2026-01-11*
