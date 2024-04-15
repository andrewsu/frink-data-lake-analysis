# Introduction

Basic analysis of identifiers used in Theme 1 KGs, looking for corresponding Wikidata items.


# Requirements
* install rclone
    * configure lakefs in `~/.config/rclone/rclone.conf`
```
     [lakefs]
     type = s3
     provider = Other
     env_auth = false
     access_key_id = xxxxxxxx
     secret_access_key = xxxxxx
     endpoint = https://frink-lakefs.apps.renci.org
     no_check_bucket = true
     force_path_style = true
```

# Basic outline

* edit `kg_list.txt`
    * first column is path on lakefs server
    * second column is local path
* run `sync_lakefx.sh`
* run `bash extract_names.sh`
