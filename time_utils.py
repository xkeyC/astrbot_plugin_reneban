# 所有时间转换都在这里
import re

_TIME_RE = re.compile(
    r"^(?=.*\d)(?:(?P<weeks>\d+)w)?(?:(?P<days>\d+)d)?(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?(?:(?P<seconds>\d+)s?)?$"
)


def timelast_format(time_last: int) -> str:
    """
    将剩余秒数格式化为易读的时间描述
    """
    if time_last < 0:
        return "已过期"
    if time_last == 0:
        return "永久"

    weeks = time_last // 604800
    days = (time_last % 604800) // 86400
    hours = (time_last % 86400) // 3600
    minutes = (time_last % 3600) // 60
    seconds = time_last % 60

    result = ["剩余"]
    if weeks > 0:
        result.append(f"{weeks}周")
    if days > 0:
        result.append(f"{days}天")
    if hours > 0:
        result.append(f"{hours}小时")
    if minutes > 0:
        result.append(f"{minutes}分钟")
    if seconds > 0 or len(result) == 1:
        result.append(f"{seconds}秒")

    return "".join(result)


def time_format(time_str: str) -> str:
    """
    将时间字符串格式化为易读的时间描述
    """
    if time_str == "0":
        return "永久"
    time = timestr_to_int(time_str)

    weeks = time // 604800
    days = (time % 604800) // 86400
    hours = (time % 86400) // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60

    result = []
    if weeks > 0:
        result.append(f"{weeks}周")
    if days > 0:
        result.append(f"{days}天")
    if hours > 0:
        result.append(f"{hours}小时")
    if minutes > 0:
        result.append(f"{minutes}分钟")
    if seconds > 0 or not result:
        result.append(f"{seconds}秒")

    return "".join(result)


def timestr_to_int(timestr: str) -> int:
    """
    将时间字符串（如 1w2d3h4m5s）转换为秒数
    """
    m = _TIME_RE.fullmatch(timestr)
    if not m:
        raise ValueError(f"非法的时间字符串格式: {timestr!r}")

    parts = {k: int(v or 0) for k, v in m.groupdict().items()}
    return (
        parts["weeks"] * 604800
        + parts["days"] * 86400
        + parts["hours"] * 3600
        + parts["minutes"] * 60
        + parts["seconds"]
    )
