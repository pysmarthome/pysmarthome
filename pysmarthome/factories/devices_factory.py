from pysmarthome.models.refs import DevicesRefModel
from pysmarthome.config import collections

from pysmarthome.controllers.devices import Tv, Ac, FloorLamp, BroadlinkDevice
from pysmarthome.controllers.devices import GoveeLedStrip
from pysmarthome.controllers.devices import Yeelight
from pysmarthome.controllers.devices import SonoffDevice
from pysmarthome.controllers.devices import Pc


class DevicesFactory:
    collections_map = {
        collections['tvs']            : Tv,
        collections['acs']            : Ac,
        collections['broadlink_lamps']: FloorLamp,
        collections['yeelights']      : Yeelight,
        collections['sonoffs']        : SonoffDevice,
        collections['pcs']            : Pc,
        collections['govee']          : GoveeLedStrip,
    }


    @staticmethod
    def load(db, id):
        try:
            c_id = DevicesRefModel.load(db, id).collection_id
            dev_cls = DevicesFactory.collections_map[c_id]
            return dev_cls.load(db, id)
        except Exception as e:
            raise e


    @staticmethod
    def load_all(db):
        devs = []
        ids = [ m.id for m in DevicesRefModel.load_all(db) ]
        for id in ids:
            devs.append(DevicesFactory.load(db, id))
        return devs
