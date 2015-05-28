README.TXT
Mario Shell Defense edited by Marc Partoriza
----
Documented comments on changes are indicated by '###' in code
Changes include:
Red fireballs now shoot straight across
Blue fireballs now have their own gravity, the red fireballs old one (Blue fireballs bounce like red ones)
All red fireballs now move at the same speed. 3 wasn't too slow nor too fast.
Changed the shell's gravity, x_vel and y_vel to mimic the old blue fireball's stats.
IMPROVEMENT: Upon death, there is now a new caption 'Time' that indicates how long you have been playing.
Added a new parameter to fireball constructor
Added key 'f' to shoot a blue fireball, key 'e' only shoots red fireballs now.
Removed self.onGround = true, to make the koopa shells bounce instead of staying on ground.