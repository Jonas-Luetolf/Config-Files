--imports
import XMonad
import Data.Monoid
import System.Exit

import XMonad.Hooks.ManageDocks

import XMonad.Layout.Spacing

import XMonad.Util.SpawnOnce
import XMonad.Util.Run

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

import Graphics.X11.ExtraTypes.XF86

import XMonad.Actions.GridSelect
import XMonad.Actions.NoBorders
--
myTerminal      = "alacritty"

myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

myClickJustFocuses :: Bool
myClickJustFocuses = False

myBorderWidth   = 4
--myXmobarrc = "~/.config/xmobar/xmobarrc"
--myConkyrc = "~/.conky/nord-01.conkyrc"
myModMask       = mod1Mask

myWorkspaces    = ["1","2","3","4","5","6","7","8","9"]

-- Border colors
myNormalBorderColor  = "#EBCB8B"
myFocusedBorderColor = "#88C0D0"

toggleFull = withFocused (\windowId -> do    
{       
   floats <- gets (W.floating . windowset);        
   if windowId `M.member` floats        
   then do 
       withFocused $ toggleBorder           
       withFocused $ windows . W.sink
   
   else do 
       withFocused $ toggleBorder           
       withFocused $  windows . (flip W.float $ W.RationalRect 0 0 1 1)    }    )
------------------------------------------------------------------------
-- Key bindings
myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

-- launch a terminal
    [ ((modm .|. shiftMask, xK_Return), spawn $ XMonad.terminal conf)


    ,((modm,               xK_f     ), toggleFull)

-- launch rofi
    , ((modm,               xK_p     ), spawn "rofi -show drun")
    , ((modm .|. shiftMask, xK_p     ), spawn "rofi -show run")

    , ((modm .|. shiftMask, xK_t     ), spawn "killall trayer")

-- close focused window
    , ((modm .|. shiftMask, xK_c     ), kill)

-- Rotate through the available layout algorithms
    , ((modm,               xK_space ), sendMessage NextLayout)

--  Reset the layouts on the current workspace to default
    , ((modm .|. shiftMask, xK_space ), setLayout $ XMonad.layoutHook conf)

-- Resize viewed windows to the correct size
    , ((modm,               xK_n     ), refresh)

-- Move focus to the next window
    , ((modm,               xK_Tab   ), windows W.focusDown)

-- Move focus to the next window
    , ((modm,               xK_j     ), windows W.focusDown)

-- Move focus to the previous window
    , ((modm,               xK_k     ), windows W.focusUp  )

-- Move focus to the master window
    , ((modm,               xK_m     ), windows W.focusMaster  )

-- Swap the focused window and the master window
    , ((modm,               xK_Return), windows W.swapMaster)

-- Swap the focused window with the next window
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown  )

-- Swap the focused window with the previous window
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp    )

-- Shrink the master area
    , ((modm,               xK_h     ), sendMessage Shrink)

-- Expand the master area
    , ((modm,               xK_l     ), sendMessage Expand)

-- Push window back into tiling
    , ((modm,               xK_t     ), withFocused $ windows . W.sink)

-- Increment the number of windows in the master area
    , ((modm              , xK_comma ), sendMessage (IncMasterN 1))

-- Deincrement the number of windows in the master area
    , ((modm              , xK_period), sendMessage (IncMasterN (-1)))

    -- Toggle the status bar gap
    -- Use this binding with avoidStruts from Hooks.ManageDocks.
    -- See also the statusBar function from Hooks.DynamicLog.
    --
    , ((modm              , xK_b     ), sendMessage ToggleStruts)

-- Quit xmonad
    , ((modm .|. shiftMask, xK_q     ), io (exitWith ExitSuccess))

-- Restart xmonad
    , ((modm              , xK_q     ), spawn "xmonad --recompile; xmonad --restart")

-- Run xmessage with a summary of the default keybindings (useful for beginners)
    , ((modm .|. shiftMask, xK_slash ), spawn ("echo \"" ++ help ++ "\" | xmessage -file -"))

-- displayct
    , ((modm .|. shiftMask, xK_d), spawn "displayctl menu")
    , ((modm .|. shiftMask, xK_a), spawn "displayctl auto")

-- controll volume
    , ((0, xF86XK_AudioRaiseVolume), spawn "pactl set-sink-volume @DEFAULT_SINK@ +5%")
    , ((0, xF86XK_AudioLowerVolume), spawn "pactl set-sink-volume @DEFAULT_SINK@ -5%")
    , ((0, xF86XK_AudioMute), spawn "pactl set-sink-mute @DEFAULT_SINK@ toggle")
    
-- controll Brightness
    , ((0, xF86XK_MonBrightnessDown), spawn "lux -s 5%")
    , ((0, xF86XK_MonBrightnessUp), spawn "lux -a 5%")
    ]
    ++

    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
        , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    ++

    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [xK_w, xK_e, xK_r] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]


------------------------------------------------------------------------
-- Mouse bindings
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))

    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))

    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))

    ]

------------------------------------------------------------------------
-- Layouts
myLayout = avoidStruts (tiled ||| Mirror tiled ||| Full)
  where
     tiled   = Tall nmaster delta ratio

     nmaster = 1

     ratio   = 1/2

     delta   = 3/100

-- Window rules
myManageHook = composeAll
    [ className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore ]

-- Event handling
myEventHook = mempty

-- Status bars and logging
myLogHook = return ()

-- Startup hook
myStartupHook = do
    spawn "killall conky"   -- kill current conky on each restart
    spawn "killall trayer"  -- kill current trayer on each restart

    spawnOnce "picom"
	spawnOnce "dunst"
    spawnOnce "nm-applet"
    spawnOnce "volumeicon"
    spawnOnce "kdeconnect-indicator"    
    spawn ("sleep 2 && conky -c $HOME/.conky/nord-01.conkyrc")
    spawn ("sleep 2 && trayer --edge top --align right --tint 0x2E3440 --width 15 --monitor 0 --transparent true --alpha 0 --height 28")

    spawnOnce "nitrogen --restore &"

main = do
  xmproc <- spawnPipe "picom"
  xmproc <- spawnPipe "xmobar -x 0 /home/jonas/.config/xmobar/xmobarrc"
  xmproc <- spawnPipe "xmobar -x 1 /home/jonas/.config/xmobar/xmobarrc"
  xmproc <- spawnPipe "xmobar -x 2 /home/jonas/.config/xmobar/xmobarrc"
  xmonad $ docks defaults


defaults = def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = spacingWithEdge 4 $ myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        logHook            = myLogHook,
        startupHook        = myStartupHook
    }

-- | Finally, a copy of the default bindings in simple textual tabular format.
help :: String
help = unlines ["The default modifier key is 'alt'. Default keybindings:",
    "",
    "-- launching and killing programs",
    "mod-Shift-Enter  Launch terminal",
    "mod-p            Launch rofi",
    "mod-Shift-c      Close/kill the focused window",
    "mod-Space        Rotate through the available layout algorithms",
    "mod-Shift-Space  Reset the layouts on the current workSpace to default",
    "mod-n            Resize/refresh viewed windows to the correct size",
    "",
    "-- move focus up or down the window stack",
    "mod-Tab        Move focus to the next window",
    "mod-Shift-Tab  Move focus to the previous window",
    "mod-j          Move focus to the next window",
    "mod-k          Move focus to the previous window",
    "mod-m          Move focus to the master window",
    "",
    "-- modifying the window order",
    "mod-Return   Swap the focused window and the master window",
    "mod-Shift-j  Swap the focused window with the next window",
    "mod-Shift-k  Swap the focused window with the previous window",
    "",
    "-- resizing the master/slave ratio",
    "mod-h  Shrink the master area",
    "mod-l  Expand the master area",
    "",
    "-- floating layer support",
    "mod-t  Push window back into tiling; unfloat and re-tile it",
    "",
    "-- increase or decrease number of windows in the master area",
    "mod-comma  (mod-,)   Increment the number of windows in the master area",
    "mod-period (mod-.)   Deincrement the number of windows in the master area",
    "",
    "-- quit, or restart",
    "mod-Shift-q  Quit xmonad",
    "mod-q        Restart xmonad",
    "mod-[1..9]   Switch to workSpace N",
    "",
    "-- Workspaces & screens",
    "mod-Shift-[1..9]   Move client to workspace N",
    "mod-{w,e,r}        Switch to physical/Xinerama screens 1, 2, or 3",
    "mod-Shift-{w,e,r}  Move client to screen 1, 2, or 3",
    "",
    "-- Mouse bindings: default actions bound to mouse events",
    "mod-button1  Set the window to floating mode and move by dragging",
    "mod-button2  Raise the window to the top of the stack",
    "mod-button3  Set the window to floating mode and resize by dragging"]
