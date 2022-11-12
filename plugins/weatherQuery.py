import httpx

API_KEY = 'SeSI8hL-BdFhE9MKb'

async def querys(city: str) -> str:
    """查询天气数据。"""
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f'https://api.seniverse.com/v3/weather/now.json', params={
                'key': API_KEY,
                'location': city,
                'language': 'zh-Hans',
                'unit': 'c',
            })
            resp.raise_for_status()
            data = resp.json()
            return f'当前{data["results"][0]["location"]["name"]}天气为' \
                f'{data["results"][0]["now"]["text"]}，' \
                f'气温{data["results"][0]["now"]["temperature"]}℃。'
        except (httpx.NetworkError, httpx.HTTPStatusError, KeyError):
            return f'抱歉，没有找到{city}的天气数据。'

