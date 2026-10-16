from typing import Any
import httpx

class SearXNGSearch:
    def __init__(self, base_url: str, timeout=10.0):
        self.base_url = base_url
        self.timeout = timeout

    async def search(self, query: str, max_results=5, language='en') -> list[dict[str, Any]]:
        if not query.strip():
            raise ValueError('Query cannot be empty.')
        if max_results < 1:
            raise ValueError('Max result must be at least 1.')

        params = {
            'q': query.strip(),
            'format': 'json',
            'language': language
        }

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f'{self.base_url}/search', params=params)
            
            response.raise_for_status()
            data = response.json()

        results = []
        for item in data.get('results', [])[:max_results]:
            results.append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'content': item.get('content', ''),
                'engine': item.get('engine', ''),
                'score': item.get('score', ''),
            })

        return results