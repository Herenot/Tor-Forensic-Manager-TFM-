class Constant:
    # Constantes para la UI
    signature = '-----BEGIN PGP SIGNATURE-----'
    executed_at = 'Executed at: '
    dialog1 = ' To preserve the evidence of the equipment under\n investigation, it is important to make a copy'
    dialog2 = ' Cancelling this operation could damage evidence\n and invalidate any judicial investigation'
    dialog3 = '----WARNING!----'
    copy_title = 'Select destination directory'
    update_yes = 'Yes, '
    update_no = '"No pending updates"'
    torrc_user = 'The content of the torrc file for user {} is shown in the following list: \n\n'
    compatibility_string = 'Shown compatibility.ini content below:\n\n'
    prefs_string = 'Shown Prefs.js content bewlow:\n\n'
    no_available_error = 'Error.No data available'
    null_data = 'No available data'
    error_dialog = 'You must have done security\ncopy to use this feature'
    intro_manage = 'Below you can see all the sqlite files under .../Browser/profile.default directory.The information\n\ncontent absolute path with its size. Moreover, you can open the artifacts/bookmarks directory and\n\ninspect them on differents web pages.'
    intro_ia = 'In this view, the signature of the hashes can be easily and quickly observed. Also, in the lower field\nyou can enter a hash to check if it is in the hash file (sha256 or md5). You can also select a file to\ncompare against the hashes of the original file.'
    not_find_hashes_files = "Files *.txt.asc don't find.\nPlease select a directory what contain them"
    not_find_coincidences = 'No hash matches found in hash file.\nProbably file has been modified or introduced hash is incorrect'
    not_find_coincidences = 'Hash found, file is intact'

    # Ubicación de las ventanas
    ppal_ui_dir = './../frontend/principal.ui'
    init_dialog_dir = './../frontend/initialDialogBox.ui'
    info_window_dir = './../frontend/infoWindow.ui'
    info_manage_dir = './../frontend/manageFiles.ui'
    info_nodes_info_dir = './../frontend/nodesInfo.ui'
    info_help_window_dir = './../frontend/helpWindow.ui'
    error_dialog_dir = './../frontend/errorDialogBox.ui'
    hashes_not_found_dialog_dir = './../frontend/hashes_dialog.ui'
    hashes_found_dialog_dir = './../frontend/hashes_dialog_ok.ui'
    ia_manage_dir = './../frontend/manageIA.ui'
    info_readme_dir = './../extraFiles/readme.txt'
    torrc_file_dir = './../frontend/torrcWindow.ui'
    prefs_string = './../frontend/prefsWindow.ui'
    compatibility_dir = './../frontend/compatibilityWindow.ui'
    
    # Ubicación archivos auxiliares
    aux_data_file = './data.txt'
    aux_elements_find_file = './find_elements.txt'
    aux_nodes_file = './nodes.txt'
    aux_artifacts_file = './artifacts.txt'
    aux_hash256 = '/aux_256.txt'
    aux_hashmd5 = '/aux_md5.txt'
    file_hash256 = '/hashes256.txt'
    file_hash256_asc = '/hashes256.txt.asc'
    file_hashmd5 = '/hashesmd5.txt'
    file_hashmd5_asc = '/hashesmd5.txt.asc'
    diff_dir = '/diff_results'

    # Operation with hashes strings
    no_matches_text = 'NO Matches found in file:\n{}'
    matches_found_text = 'Matches!.File with that hash:\n{}'
    same_hashes_text = 'Hashes are the same.'
    explanation_text = '"\t\t======= Differences =======\n\n'
