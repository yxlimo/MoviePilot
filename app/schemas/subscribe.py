import json
from typing import Optional, List, Dict, Any

from pydantic import BaseModel, validator


class Subscribe(BaseModel):
    id: Optional[int] = None
    # 订阅名称
    name: Optional[str] = None
    # 订阅年份
    year: Optional[str] = None
    # 订阅类型 电影/电视剧
    type: Optional[str] = None
    # 搜索关键字
    keyword: Optional[str] = None
    tmdbid: Optional[int] = None
    doubanid: Optional[str] = None
    bangumiid: Optional[int] = None
    # 季号
    season: Optional[int] = None
    # 海报
    poster: Optional[str] = None
    # 背景图
    backdrop: Optional[str] = None
    # 评分
    vote: Optional[int] = 0
    # 描述
    description: Optional[str] = None
    # 过滤规则
    filter: Optional[str] = None
    # 包含
    include: Optional[str] = None
    # 排除
    exclude: Optional[str] = None
    # 质量
    quality: Optional[str] = None
    # 分辨率
    resolution: Optional[str] = None
    # 特效
    effect: Optional[str] = None
    # 总集数
    total_episode: Optional[int] = 0
    # 开始集数
    start_episode: Optional[int] = 0
    # 缺失集数
    lack_episode: Optional[int] = 0
    # 附加信息
    note: Optional[Any] = None
    # 状态：N-新建， R-订阅中
    state: Optional[str] = None
    # 最后更新时间
    last_update: Optional[str] = None
    # 订阅用户
    username: Optional[str] = None
    # 订阅站点
    sites: Optional[List[int]] = []
    # 是否洗版
    best_version: Optional[int] = 0
    # 当前优先级
    current_priority: Optional[int] = None
    # 保存路径
    save_path: Optional[str] = None
    # 是否使用 imdbid 搜索
    search_imdbid: Optional[int] = 0
    # 时间
    date: Optional[str] = None

    @validator('sites', pre=True)
    def parse_json_fields(cls, value):
        if value:
            if isinstance(value, str):
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    return []
            return value
        return []

    class Config:
        orm_mode = True


class SubscribeDownloadFileInfo(BaseModel):
    # 种子名称
    torrent_title: Optional[str] = None
    # 站点名称
    site_name: Optional[str] = None
    # 下载器
    downloader: Optional[str] = None
    # hash
    hash: Optional[str] = None
    # 文件路径
    file_path: Optional[str] = None


class SubscribeLibraryFileInfo(BaseModel):
    # 存储
    storage: Optional[str] = "local"
    # 文件路径
    file_path: Optional[str] = None


class SubscribeEpisodeInfo(BaseModel):
    # 标题
    title: Optional[str] = None
    # 描述
    description: Optional[str] = None
    # 背景图
    backdrop: Optional[str] = None
    # 下载文件信息
    download: Optional[List[SubscribeDownloadFileInfo]] = []
    # 媒体库文件信息
    library: Optional[List[SubscribeLibraryFileInfo]] = []


class SubscrbieInfo(BaseModel):
    # 订阅信息
    subscribe: Optional[Subscribe] = None
    # 集信息 {集号: {download: 文件路径，library: 文件路径, backdrop: url, title: 标题, description: 描述}}
    episodes: Optional[Dict[int, SubscribeEpisodeInfo]] = {}
