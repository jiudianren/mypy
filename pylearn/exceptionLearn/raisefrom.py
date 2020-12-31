
    try:
        extract_dirs = extract_collection(config.get_cfg_file_is_zip_dir(),
                                          config.get_cfg_file_zip_dir(),
                                          config.get_cfg_file_zip_files(),
                                          config.get_cfg_file_unzip_dir())
    except Exception as e:
        logging.exception(e)
        raise RuntimeError("EXTRACT COLLECTION "+ get_tb_info(e)) from e
    else:
        logging.debug(f"PROCESS extract_collection OK")
