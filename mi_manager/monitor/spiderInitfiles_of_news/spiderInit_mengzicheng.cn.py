# -*- coding: utf-8 -*-
import redis
def init():
    print "pushing mengzicheng.cn:start_url......"
    try:
        r = redis.Redis("192.168.139.239", 7001, 0)
        r.delete("mengzicheng.cn:start_urls")
        r.delete("mengzicheng.cn:dupefilter" + "0")
        r.delete("mengzicheng.cn:requests")
        r.lpush("mengzicheng.cn:start_urls", 'http://www.mengzicheng.cn/wordpress/wp-admin/post.php?post=1106&action=edit')
        r2 = redis.Redis("192.168.139.239", 7001, 15)
        for keyname in 'downloader/request_count', 'downloader/response_count', 'downloader/response_status_count/200', 'item_scraped_count':
            r2.delete(keyname + "_" + "mengzicheng.cn")
        print "pushing mengzicheng.cn:start_url success"
    except Exception:
        print "pushing mengzicheng.cn:start_url failed"
if __name__ == '__main__':
    init()