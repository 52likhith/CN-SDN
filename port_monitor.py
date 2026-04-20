from pox.core import core
import pox.openflow.libopenflow_01 as of
import datetime

log = core.getLogger()

class PortMonitor(object):

    def __init__(self):
        core.openflow.addListeners(self)
        self.port_status = {}

    def _handle_PortStatus(self, event):
        dpid = event.dpid
        port_no = event.ofp.desc.port_no
        reason = event.ofp.reason

        # Determine status
        if reason == of.OFPPR_ADD:
            status = "UP"
        elif reason == of.OFPPR_DELETE:
            status = "DOWN"
        elif reason == of.OFPPR_MODIFY:
            if event.ofp.desc.state & of.OFPPS_LINK_DOWN:
                status = "DOWN"
            else:
                status = "UP"
        else:
            status = "UNKNOWN"

        # Store status
        self.port_status[(dpid, port_no)] = status

        log_msg = f"{datetime.datetime.now()} | Switch {dpid} Port {port_no} → {status}"
        print(log_msg)

        # Save to file
        with open("port_log.txt", "a") as f:
            f.write(log_msg + "\n")

        # Alert
        if status == "DOWN":
            print("⚠️ ALERT: Port DOWN detected!")

        self.display_status()

    def display_status(self):
        print("\n==== Current Port Status ====")
        for (dpid, port), status in self.port_status.items():
            print(f"Switch {dpid} Port {port} → {status}")
        print("============================\n")


def launch():
    core.registerNew(PortMonitor)
