from enum import IntEnum


class Classes(IntEnum):
    CLASS_WARRIOR = 1
    CLASS_PALADIN = 2
    CLASS_HUNTER = 3
    CLASS_ROGUE = 4
    CLASS_PRIEST = 5
    CLASS_SHAMAN = 7
    CLASS_MAGE = 8
    CLASS_WARLOCK = 9
    CLASS_DRUID = 11


class Races(IntEnum):
    RACE_HUMAN = 1
    RACE_ORC = 2
    RACE_DWARF = 3
    RACE_NIGHT_ELF = 4
    RACE_UNDEAD = 5
    RACE_TAUREN = 6
    RACE_GNOME = 7
    RACE_TROLL = 8


class CreatureTypes(IntEnum):
    BEAST = 1
    DRAGON = 2
    DEMON = 3
    ELEMENTAL = 4
    GIANT = 5
    UNDEAD = 6
    HUMANOID = 7
    AMBIENT = 8  # Critter
    MECHANICAL = 9
    NOT_SPECIFIED = 10


# Also known as CreatureDifficultyFlags.
# Used internally but Blizzlike.
class CreatureStaticFlags(IntEnum):
    MOUNTABLE = 1  # Has proper mount points?
    NO_XP = 2  # Gives no XP on death.
    NO_LOOT = 4  # Generates no loot on death.
    UNKILLABLE = 8  # Can't be killed.
    TAMEABLE = 16  # Is tameable.
    IMMUNE_PLAYER = 32  # Is immune to player attacks.
    IMMUNE_NPC = 64  # Is immune to other NPC attacks.
    CAN_WIELD_LOOT = 128
    SESSILE = 256  # Creature always rooted?
    UNSELECTABLE = 512
    NO_AUTO_REGEN = 1024  # Shouldn't regenerate health and power on evade?
    CORPSE_NONE = 2048  # Don't leave corpse?
    CORPSE_RAID = 4096
    CREATOR_LOOT = 8192  # Lootable only by creator (like dummies).
    NO_DEFENSE = 16384  # No defense to melee attacks?
    NO_SPELL_DEFENSE = 32768  # No defense to spell attacks?
    TABARD_VENDOR = 65536  # Flag carried by Tabard Vendor NPCS? Was later reused as "Raid Boss".
    COMBAT_PING = 131072  # Seems to be only used by Sentry Totem NPC.
    AQUATIC = 262144  # Can only move in water.
    AMPHIBIOUS = 524288  # Can enter water and walk on terrain.
    NO_MELEE = 1048576  # Prevents melee, mostly used by totems.


class Genders(IntEnum):
    GENDER_MALE = 0
    GENDER_FEMALE = 1


class Teams(IntEnum):
    TEAM_NONE = 0
    TEAM_CROSSFACTION = 1
    TEAM_HORDE = 67
    TEAM_ALLIANCE = 469


class PowerTypes(IntEnum):
    TYPE_HEALTH = -2
    TYPE_MANA = 0
    TYPE_RAGE = 1
    TYPE_FOCUS = 2
    TYPE_ENERGY = 3
    TYPE_HAPPINESS = 4


class UnitFlags(IntEnum):
    UNIT_FLAG_STANDARD = 0x00000000
    UNIT_FLAG_FROZEN4 = 0x00000001
    UNIT_FLAG_FROZEN = 0x00000004
    UNIT_FLAG_DUELING = 0x00000008
    UNIT_FLAG_PLUS_MOB = 0x00000040
    UNIT_FLAG_NOT_ATTACKABLE_OCC = 0x00000100
    UNIT_FLAG_PASSIVE = 0x00000200
    UNIT_FLAG_LOOTING = 0x00000400
    UNIT_FLAG_PET_IN_COMBAT = 0x00000800
    UNIT_FLAG_MOUNT_ICON = 0x00001000
    UNIT_FLAG_MOUNT = 0x00002000
    UNIT_FLAG_DEAD = 0x00004000
    UNIT_FLAG_SNEAK = 0x00008000
    UNIT_FLAG_GHOST = 0x000010000
    UNIT_FLAG_PACIFIED = 0x000020000
    UNIT_FLAG_DISABLE_ROTATE = 0x00040000
    UNIT_FLAG_IN_COMBAT = 0x00080000
    UNIT_FLAG_TAXI_FLIGHT = 0x00100000
    UNIT_FLAG_DISARMED = 0x00200000
    UNIT_FLAG_CONFUSED = 0x00400000
    UNIT_FLAG_FLEEING = 0x00800000
    UNIT_FLAG_POSSESSED = 0x01000000
    UNIT_FLAG_SKINNABLE = 0x04000000
    UNIT_FLAG_SHEATHE = 0x40000000

    UNIT_MASK_MOUNTED = UNIT_FLAG_MOUNT_ICON | UNIT_FLAG_MOUNT
    UNIT_MASK_DEAD = UNIT_FLAG_DEAD | UNIT_FLAG_PACIFIED | UNIT_FLAG_DISABLE_ROTATE
    UNIT_MASK_NON_ATTACKABLE = UNIT_FLAG_NOT_ATTACKABLE_OCC | UNIT_FLAG_PASSIVE


class StandState(IntEnum):
    UNIT_STANDING = 0x0
    UNIT_SITTING = 0x1
    UNIT_SITTINGCHAIR = 0x2
    UNIT_SLEEPING = 0x3
    UNIT_SITTINGCHAIRLOW = 0x4
    UNIT_FIRSTCHAIRSIT = 0x4
    UNIT_SITTINGCHAIRMEDIUM = 0x5
    UNIT_SITTINGCHAIRHIGH = 0x6
    UNIT_LASTCHAIRSIT = 0x6
    UNIT_DEAD = 0x7
    UNIT_KNEEL = 0x8


class UnitReaction(IntEnum):
    UNIT_REACTION_HATED = 0
    UNIT_REACTION_HOSTILE = 1
    UNIT_REACTION_UNFRIENDLY = 2
    UNIT_REACTION_NEUTRAL = 3
    UNIT_REACTION_AMIABLE = 4
    UNIT_REACTION_FRIENDLY = 5
    UNIT_REACTION_REVERED = 6


class UnitSummonType(IntEnum):
    UNIT_SUMMON_PET = 0
    UNIT_SUMMON_MINION = 1
    UNIT_SUMMON_CHARM = 2
    UNIT_SUMMON_GUARDIAN = 3
    UNIT_SUMMON_CREATION = 4


class WeaponMode(IntEnum):
    NORMALMODE = 0x0
    SHEATHEDMODE = 0x1
    RANGEDMODE = 0x2
    NUMMODES = 0x3


class MovementTypes(IntEnum):
    IDLE = 0x0
    WANDER = 0x1
    WAYPOINT = 0x2


# This is from 1.12, might be wrong
class ObjectSpawnFlags(IntEnum):
    SPAWN_FLAG_ACTIVE = 0x01
    SPAWN_FLAG_DISABLED = 0x02
    SPAWN_FLAG_RANDOM_RESPAWN_TIME = 0x04
    SPAWN_FLAG_DYNAMIC_RESPAWN_TIME = 0x08
    SPAWN_FLAG_FORCE_DYNAMIC_ELITE = 0x10  # creature only
    SPAWN_FLAG_EVADE_OUT_HOME_AREA = 0x20  # creature only
    SPAWN_FLAG_NOT_VISIBLE = 0x40  # creature only


# Used in SMSG_MONSTER_MOVE
class SplineFlags(IntEnum):
    SPLINEFLAG_NONE = 0x00000000
    SPLINEFLAG_DONE = 0x000000001
    SPLINEFLAG_FALLING = 0x000000002  # Affects elevation computation
    SPLINEFLAG_RUNMODE = 0x00000100
    SPLINEFLAG_FLYING = 0x00000200  # Smooth movement(Catmullrom interpolation mode), flying animation
    SPLINEFLAG_NOSPLINE = 0x00000400
    SPLINEFLAG_SPLINE = 0x00002000  # Spline n * (float xyz)
    SPLINEFLAG_SPOT = 0x00010000
    SPLINEFLAG_TARGET = 0x00020000
    SPLINEFLAG_FACING = 0x00040000
    SPLINEFLAG_CYCLIC = 0x00100000  # Movement by cycled spline
    SPLINEFLAG_ENTER_CYCLE = 0x00200000  # Appears with cyclic flag in monster move packet, erases first spline vertex after first cycle done
    SPLINEFLAG_FROZEN = 0x00400000  # Will never arrive


# Used in SMSG_MONSTER_MOVE
class SplineType(IntEnum):
    SPLINE_TYPE_NORMAL = 0
    SPLINE_TYPE_STOP = 1
    SPLINE_TYPE_FACING_SPOT = 2
    SPLINE_TYPE_FACING_TARGET = 3
    SPLINE_TYPE_FACING_ANGLE = 4


# Internal usage, custom values.
class UnitStates(IntEnum):
    NONE = 0x00000000
    ROOTED = 0x00000001
    STUNNED = 0x00000002
    POSSESSED = 0x00000004
    DISTRACTED = 0x00000008
    CONFUSED = 0x00000010
    FOLLOWING = 0x00000020
    FLEEING = 0x00000040
