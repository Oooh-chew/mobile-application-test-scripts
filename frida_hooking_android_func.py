import sys
import frida

TARGET = "org.mozilla.firefox"
TARGET_CLASS = ""


def on_message(message, data):
    if message['type'] == 'send':
        print("🐵 {0}".format(message['payload']))
    elif message['type'] == 'error':
        # give color and formatter
        print("🐞🐞🐞")
        for k, v in message.items():
            print('[!]' + k + "= " + str(v))
    else:
        print(message)


js = """
Java.perform(function () {
    // Target Class
    var queryClass = Java.use("androidx.room.RoomSQLiteQuery");

    // Hooking target function
    queryClass.acquire.overload('java.lang.String', 'int').implementation = function(x, y) {
        send("RoomSQLiteQuery acquire HIT!");
        send("x = " + x);
        send("y = " + y);

        var result = this.acquire(x, y);

        console.log("result = " + result.toString());
        console.log("query = " + result.mQuery.value);

        return result
    };
});
"""


device = frida.get_usb_device()
pid = device.spawn([TARGET])
session = device.attach(pid)
script = session.create_script(js)
script.on('message', on_message)
script.load()
device.resume(pid)
sys.stdin.read()
