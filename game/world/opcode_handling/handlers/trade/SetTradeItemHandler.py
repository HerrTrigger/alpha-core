from struct import unpack

from game.world.managers.objects.player.TradeManager import TradeManager
from utils.constants.ItemCodes import InventorySlots
from utils.constants.ObjectCodes import TradeStatuses


class SetTradeItemHandler(object):

    @staticmethod
    def handle(world_session, socket, reader):
        if not world_session.player_mgr.trade_data:
            return 0

        if len(reader.data) >= 3:  # Avoid handling empty set trade item packet
            trade_slot, bag, slot = unpack('<3B', reader.data)
            if bag == 0xFF or bag == InventorySlots.SLOT_BANK_END:
                bag = InventorySlots.SLOT_INBACKPACK.value
            item = world_session.player_mgr.inventory.get_item(bag, slot)
            if not item:
                return 0

            if trade_slot > TradeManager.TradeData.TRADE_SLOT_COUNT:
                TradeManager.send_trade_status(world_session.player_mgr, TradeStatuses.TRADE_STATUS_CANCELLED)
                return 0

            world_session.player_mgr.trade_data.set_item(trade_slot, item)

        return 0