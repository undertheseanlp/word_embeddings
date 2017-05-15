from dirsync import sync
sourcedir = "crawl_vn_news/vn_news/data"
targetdir = "data"
sync(sourcedir, targetdir, "sync")