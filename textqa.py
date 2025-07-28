from aift import setting
setting.set_api_key('WKg1RaHAFQdrfFjrsLosdGbBxRSllGVk')

from aift.multimodal import textqa 
result = textqa.generate('กินอะไรดีเที่ยงนี้? ขอแบบพิศดาร')

print(result['content'])