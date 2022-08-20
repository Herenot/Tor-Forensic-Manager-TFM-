class Constant:
    # Constantes para la UI
    signature = '-----BEGIN PGP SIGNATURE-----'
    executed_at = 'Executed at: '
    dialog1 = ' To preserve the evidence of the equipment under\n investigation, it is important to make a copy.'
    dialog2 = ' Cancelling this operation could damage evidence\n and invalidate any judicial investigation.'
    dialog3 = '----WARNING!----'
    copy_title = 'Select destination directory'
    update_yes = 'Yes, '
    update_no = '"No pending updates"'
    torrc_user = 'The content of the torrc file for user {} is shown in the following list: \n\n'
    compatibility_string = 'Shown compatibility.ini content below:\n\n'
    prefs_string = 'Shown Prefs.js content bewlow:\n\n'
    no_available_error = 'Error.No data available.'
    null_data = 'No available data'
    error_dialog = 'You must have done security\ncopy to use this feature'
    intro_manage = 'Below you can see all the sqlite files under .../Browser/profile.default directory.The information\n\ncontent absolute path with its size. Moreover, you can open the artifacts/bookmarks directory and\n\ninspect them on differents web pages.'
    intro_ia = 'In this view, the signature of the hashes can be easily and quickly observed. Also, in the lower field\nyou can enter a hash to check if it is in the hash file (sha256 or md5). You can also select a file to\ncompare against the hashes of the original file.'
    not_find_hashes = "Files *.txt.asc don't find.\nPlease select a directory what contain them"

    # Ubicación de las ventanas
    ppal_ui_dir = './frontend/principal.ui'
    init_dialog_dir = './frontend/initialDialogBox.ui'
    info_window_dir = './frontend/infoWindow.ui'
    info_manage_dir = './frontend/manageFiles.ui'
    info_nodes_info_dir = './frontend/nodesInfo.ui'
    info_help_window_dir = './frontend/helpWindow.ui'
    error_dialog_dir = './frontend/errorDialogBox.ui'
    ia_manage_dir = './frontend/manageIA.ui'
    info_readme_dir = './extraFiles/readme.txt'
    


    # Ubicación archivos auxiliares
    aux_data_file = './data.txt'
    aux_elements_find_file = './find_elements.txt'
    aux_nodes_file = './nodes.txt'
    aux_artifacts_file = './artifacts.txt'