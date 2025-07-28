from aift import setting
from aift.multimodal import vqa
 
setting.set_api_key('WKg1RaHAFQdrfFjrsLosdGbBxRSllGVk')


result = vqa.generate('japan.jpg', 'ที่นี่คือที่ไหน และดอกไม้คือดอกอะไร')
print(result)