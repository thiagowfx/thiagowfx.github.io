
I successfully upgraded my Android phone from Jelly Bean (4.1.2) to Kit Kat
(4.4.2). Here are notes about my upgrade process.

## Key steps

1. **Backup your data** before trying anything! Make sure it's available
   elsewhere—cloud or computer.

2. **Make screenshots** of installed apps: press Volume Down + Power buttons
   together for a while. Save these screenshots!

3. **Did you backup your data?** (Really!)

4. **Is your bootloader unlocked?** If not, unlock it first. See the XDA
   Developer Forums.

5. **Is your device rooted?** Maybe root it first. See the XDA Developer Forums.

6. **What do you want to do?**
   - Upgrade Android version? Search for "OTA upgrade"
   - Customize it? Search for "custom ROM"

7. **Get a decent recovery**. TWRP (Team Win Recovery Project) is one of the
   best. CWM is another option. A recovery is useful for flashing ZIPs, wiping
   cache, installing custom ROMs, and other maintenance.

8. **Reboot into bootloader with adb**: `adb reboot-bootloader`

9. **Or reboot into recovery**: `adb reboot recovery`

10. **While in fastboot**, you cannot use adb.

11. **Get updated adb**: ftp://ftp.mozilla.org/pub/labs/android-tools/

12. **Upgrade from Windows or Linux**: Usually you can do both. Windows is
    common among power Android developers. Use what's available and recommended
    by your tutorial.

13. **Don't install blindly**: Read, read, and read before anything! Check
    opinions of other users.

14. **Need support?** Use:
    - IRC (Freenode: #android-root channel)
    - Facebook Groups
    - Google+ Groups
    - Reddit
    - Search for groups about your phone model first
    - XDA Forums (technical/advanced place—don't ask newbie questions unless
      there's a specific section)

15. **Debloating** is a good term to search for after installing/upgrading your
    device.

16. **Google Play** isn't the only option. See F-Droid (contains FOSS software).

17. **Only upgrade with a charger** connected.

18. **Don't install untested or poorly tested ROMs**. It's better not to install
    anything than install something that doesn't work well. Use your head and
    inspect context carefully.

These items sum up key points. If you want to complement this post, feel free to
leave a comment. Happy hacking!

## Footnotes

- Device: Motorola Razr I XT890, with Intel Atom (x86) CPU and 1GB RAM
- XDA Developer Forums: http://forum.xda-developers.com/

