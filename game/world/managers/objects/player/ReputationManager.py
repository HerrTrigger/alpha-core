from struct import pack
from utils.constants.UnitCodes import UnitReaction
from database.realm.RealmDatabaseManager import RealmDatabaseManager
from network.packet.PacketWriter import PacketWriter
from utils.constants.ObjectCodes import ReputationFlag
from utils.constants.OpCodes import OpCode


# TODO: In the future, each player should have its own ReputatoinManager, taking care of individual states.
#  Still, it looks like rep system was practically barebones, we need more information.
class ReputationManager(object):

    @staticmethod
    def send_player_reputations(player_mgr):
        # Let the client initialize its internal faction db.
        data = pack('<I', 64)  # Client always except 64 factions.
        for i in range(0, 64):
            data += pack('<Bi', 0, 0)

        packet = PacketWriter.get_packet(OpCode.SMSG_INITIALIZE_FACTIONS, data)
        player_mgr.session.enqueue_packet(packet)

        # Send our current standings and make reputations visible.
        reputations = RealmDatabaseManager.charater_get_reputations(player_mgr.player)
        for reputation in reputations:
            data = pack('<3i', 1, reputation.index, reputation.standing)
            packet = PacketWriter.get_packet(OpCode.SMSG_SET_FACTION_STANDING, data)
            player_mgr.session.enqueue_packet(packet)  # Standing
            packet = PacketWriter.get_packet(OpCode.SMSG_SET_FACTION_VISIBLE, pack('<I', reputation.index))
            player_mgr.session.enqueue_packet(packet)  # Visible

    @staticmethod
    def get_reputation_flag(faction):
        reaction = ReputationManager.get_reaction(faction)
        if reaction < UnitReaction.UNIT_REACTION_UNFRIENDLY:
            return int(ReputationFlag.ATWAR)
        else:
            return int(ReputationFlag.HIDDEN)

    @staticmethod
    def get_standing(faction):
        return faction.reputation_base_value

    @staticmethod
    def get_reaction(faction):
        standing = ReputationManager.get_standing(faction)

        if standing >= 2100:
            return UnitReaction.UNIT_REACTION_REVERED
        elif standing >= 900:
            return UnitReaction.UNIT_REACTION_FRIENDLY
        elif standing >= 300:
            return UnitReaction.UNIT_REACTION_AMIABLE
        elif standing >= 0:
            return UnitReaction.UNIT_REACTION_NEUTRAL
        elif standing >= -300:
            return UnitReaction.UNIT_REACTION_UNFRIENDLY
        elif standing >= -600:
            return UnitReaction.UNIT_REACTION_HOSTILE
        else:
            return UnitReaction.UNIT_REACTION_HATED