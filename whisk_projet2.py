import requests, json, os, time, random, base64
BEARER_TOKEN = "Bearer ya29.a0Aa7MYio549mRxRpNAAayve_FhgOhU7HWPDPx4LhFzgnT--5y5Z8HGsnmnZrdO4qUWMtC237ce6nU1JUII2Ae1RQOAGWjTQebvZrxOW2Z5hnuf2hZwF_h17DmRXyIEVlTp_WxkLSj6GqQXwD97V6_bsH8RNUWrghUMBRw8CDOUmJy7Mg-w9cNvXrOiuxY1kxXJwARTr40Pph7JaFwa0FewQxs2M2GkmhiHuBA3M_62SyZGFqx3AIursxtZPGx3FQHJbXFtbYkDSHFx0RsUdVbDNDxNhMRcd9tAje0DtsYcKtRff57km8IGF_CJ60nbDvLHKoBSEKb3IuBoqFi0VQ9Y4Szb6fQju6WNBy2tABQd0G7aCgYKAe8SARMSFQHGX2MiKsKXDanL15GSolg9EPGPVA0371"
WORKFLOW_ID = "b0c9d4bc-1543-4556-b427-8804028339ea"
SUBJECT_ID = "CAMaJGIwYzlkNGJjLTE1NDMtNDU1Ni1iNDI3LTg4MDQwMjgzMzllYSIDQ0JBKiQ1ZWMwNjBmMy03ZDk2LTRhNmEtYTM4ZC05YTJhNDFjNGQyMTY"
SUBJECT_CAPTION = "Amara 19 ans jeune artiste West African woman natural short hair paint stains warm golden tones"
STYLE_ID = "CAMaJGIwYzlkNGJjLTE1NDMtNDU1Ni1iNDI3LTg4MDQwMjgzMzllYSIDQ0FFKiRjMzBhY2UyNy03YTNhLTQ4NWUtOGNjMS1mOWZiNGU1YzM2N2Y"
STYLE_CAPTION = "Illustration digitale semi-realiste style animation cinematographique moderne"
ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"
OUTPUT_DIR = os.path.expanduser("~/storage/downloads/whisk_projet2")
API_URL = "https://aisandbox-pa.googleapis.com/v1/whisk:runImageRecipe"
HEADERS = {"Authorization": BEARER_TOKEN, "Content-Type": "application/json"}
DELAY_MIN = 8
DELAY_MAX = 15
PROMPTS = [
"Dramatic close-up of a stern West African woman pointing at a small girl in worn clothes",
"A cold-faced West African woman looming over a small frightened girl in a wealthy home entrance",
"A 9-year-old West African girl standing frozen in a doorway hearing words of rejection",
"Portrait of Amara enormous dark eyes carrying deep sadness short unkempt natural hair",
"A young West African woman Efua lying ill in a modest bed warm late-afternoon light",
"Intimate nighttime scene a West African mother holding her small daughter candlelight warmth",
"Portrait of Tante Adjoa tall commanding West African woman expensive colorful kente-style pagne",
"Night interior narrow service corridor thin worn mattress on the bare floor dim lightbulb",
"Before-dawn a 9-year-old girl sweeping a large courtyard in darkness broom too tall for her",
"Two girls in rich school uniforms walking past a small girl mopping the floor inherited arrogance",
"A small girl eating alone in a kitchen corner half-eaten bread eyes downcast",
"Mr Kofi Mensah warm intelligent eyes behind round glasses holding a worn art textbook",
"Mr Mensah walking between desks distributing blank sheets and colored pencils morning light",
"A 9-year-old girl bent over a blank white sheet completely still staring at the paper",
"Mr Mensah frozen mid-step looking down at a child drawing with visible awe",
"Mr Mensah eyes radiating genuine recognition and warmth looking at a 9-year-old girl",
"Mr Mensah forming the words Tu as un don two life-changing words warm classroom light",
"After-school Mr Mensah sitting across from Amara asking calm questions warm afternoon light",
"A 9-year-old girl touching a paintbrush for the first time something waking inside her",
"Tante Adjoa holding up crumpled children drawings cold anger dropping them into a waste bin",
"A 9-year-old girl lying on thin mattress silent tears sliding down her temples moonlight",
"A small girl secretly drawing on a cereal box using a broken pencil stub hidden in dark",
"Mr Mensah at his desk noticing the papers he gave Amara are gone slight frown",
"A West African care home exterior clean house proper garden children drawings visible through window",
"Amara first night at care home lying in a real bed eyes open adjusting to unfamiliar comfort",
"Amara arriving at modern art school campus in Accra Ghana looking up with awe and wonder",
"Amara standing alone in a proper gallery space in Accra total absorption and reverence",
"Amara working late at night drawings showing new precision techniques learned in Accra",
"Mr Mensah at home selecting children drawings placing them in envelope writing address",
"Mr Mensah reading a letter expression changing from neutral to disbelief to profound emotion",
"Mr Mensah walking up driveway of Tante Adjoa home documents in hand professional confidence",
"Tante Adjoa sitting on sofa arms crossed cold suspicious Mr Mensah seated across from her",
"Mr Mensah standing at golden gate documents under arm face showing quiet determination",
"Amara at 16 receiving official letter from care home director hands slightly trembling",
"Amara eyes moving across words of acceptance letter expression moving to overwhelming joy",
"Art school studio in Abidjan Amara working with fierce discipline layers of paintings",
"A large format painting by Amara West African woman carrying invisible enormous weight",
"Opening night of Amara first solo exhibition gallery packed with elegantly dressed guests",
"Mr Mensah standing alone watching Amara receive recognition his eyes glistening",
"Amara spotting Mr Mensah across the gallery their eyes meeting a moment of recognition",
"Amara embracing Mr Mensah tightly long silent embrace artist and teacher who saw her first",
"Tante Adjoa moving slowly through exhibition her arrogance absent replaced by shame",
"Amara and Tante Adjoa standing before the corridor painting shame too large for language",
"Amara turning her back on Tante Adjoa walking back into gallery crowd at peace",
"Amara at 25 stepping off a plane in Paris calm readiness portfolio in carry-on",
"Inside Paris gallery thirty large-format paintings of African women on white walls",
"A small girl in service corridor transforms into woman standing in international galleries",
"Amara in a studio eyes closed before beginning work blank canvas before her",
"Mr Mensah placing pencil box in Amara hands the teacher and the artist together",
"Final image Amara and Mr Mensah seated together award between them pencil box in his hands",
]
def find_b64(obj, results):
 if isinstance(obj, dict):
  for k, v in obj.items():
   if k in ['encodedImage','imageBytes','data','image'] and isinstance(v, str) and len(v) > 200:
    results.append(v)
   else:
    find_b64(v, results)
 elif isinstance(obj, list):
  for item in obj:
   find_b64(item, results)
def save_images(data, index):
 saved = 0
 b64_list = []
 find_b64(data, b64_list)
 for i, b64 in enumerate(b64_list):
  try:
   path = f"{OUTPUT_DIR}/image_{index:04d}_{i+1}.jpg"
   with open(path, 'wb') as f:
    f.write(base64.b64decode(b64))
   print(f"  Sauvegarde: image_{index:04d}_{i+1}.jpg")
   saved += 1
  except Exception as e:
   print(f"  Erreur: {e}")
 return saved
def run():
 os.makedirs(OUTPUT_DIR, exist_ok=True)
 print(f"\n=== WHISK PROJET 2 - {len(PROMPTS)} prompts ===\n")
 success = 0
 for i, prompt in enumerate(PROMPTS):
  print(f"[{i+1}/{len(PROMPTS)}] {prompt[:60]}...")
  payload = {"clientContext": {"workflowId": WORKFLOW_ID, "tool": "BACKBONE", "sessionId": str(int(time.time()*1000))}, "seed": random.randint(100000, 999999), "imageModelSettings": {"imageModel": "GEM_PIX", "aspectRatio": ASPECT_RATIO}, "userInstruction": prompt, "recipeMediaInputs": [{"caption": SUBJECT_CAPTION, "mediaInput": {"mediaCategory": "MEDIA_CATEGORY_SUBJECT", "mediaGenerationId": SUBJECT_ID}}, {"caption": STYLE_CAPTION, "mediaInput": {"mediaCategory": "MEDIA_CATEGORY_STYLE", "mediaGenerationId": STYLE_ID}}]}
  try:
   r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
   if r.status_code == 200:
    imgs = save_images(r.json(), i+1)
    if imgs == 0:
     with open(f"{OUTPUT_DIR}/debug_{i+1:04d}.json", "w") as f:
      json.dump(r.json(), f)
     print("  OK debug JSON sauvegarde")
    success += 1
   elif r.status_code == 401:
    print("  Token expire!")
    break
   elif r.status_code == 429:
    print("  Rate limit pause 60s...")
    time.sleep(60)
   else:
    print(f"  Erreur {r.status_code}")
  except Exception as e:
   print(f"  Erreur: {e}")
  if i < len(PROMPTS) - 1:
   d = random.randint(DELAY_MIN, DELAY_MAX)
   print(f"  Pause {d}s...")
   time.sleep(d)
 print(f"\n=== TERMINE - {success}/{len(PROMPTS)} reussis ===")
run()
