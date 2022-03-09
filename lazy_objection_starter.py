#!/usr/bin/env python3

import sys
import pexpect

###############################################################################
target = ""
# [e.g.] "org.mozilla.firefox"
methods = []
# [e.g.] "org.mozilla.fenix.IntentReceiverActivity.onCreate",
classes = []
# [e.g.] "org.mozilla.fenix.crashes.CrashListActivity",
# [Info] More then two class hooking could crash an application

###############################################################################
SPAWN_OBJECTION = "objection --gadget {} explore"
HOOKING_WATCH_METHOD = "android hooking watch class_method {}\
 --dump-args --dump-backtrace --dump-return"
HOOKING_WATCH_CLASS = "android hooking watch class {}\
 --dump-args --dump-return"
ETCETERA = []

###############################################################################
if not target:
    print("target is not defined. Exiting...")
    sys.exit()

# spawn a objection
obj = pexpect.spawn(SPAWN_OBJECTION.format(target))

if obj.isalive() and obj.waitnoecho():
    # hooking (watch) methods
    if methods:
        for m in methods:
            obj.sendline(HOOKING_WATCH_METHOD.format(m))

    # hooking (watch) class
    if classes:
        for c in classes:
            obj.sendline(HOOKING_WATCH_CLASS.format(c))

    if ETCETERA:
        for e in ETCETERA:
            obj.sendline(e)

obj.interact()
