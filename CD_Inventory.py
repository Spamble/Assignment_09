#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# BEagleJack, 2021-Mar-13, added submenu for tracks
# BEagleJack, 2021-Mar-12, added error handling
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstOfCDObjects = []
lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
try:
    lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
except Exception as e:
    print(e)
while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        try:
            PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        except Exception as e:
            print(e)
            continue
        else:
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album ID: ')
        try:
            cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        except Exception as e:
            print(e)
            continue
        # start sub menu
        while True:
            IO.ScreenIO.print_CD_menu()
            cdStrChoice = IO.ScreenIO.menu_CD_choice()
            if cdStrChoice == 'x':
                break
            if cdStrChoice == 'a':
                tracks = IO.ScreenIO.get_track_info()
                try:
                    PC.DataProcessor.add_track(tracks, cd)
                except Exception as e:
                    print(e)
                continue    
            elif cdStrChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                rt = input('Select the CD / Album index: ')
                try:
                    cd.rmv_track(rt)
                except Exception as e:
                    print(e)
                continue
            elif cdStrChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            else:
                print('General Error')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')