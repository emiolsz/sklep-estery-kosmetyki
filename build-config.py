from pathlib import Path
import json
root=Path(__file__).resolve().parent
config=json.loads((root/'store-config.json').read_text(encoding='utf-8'))
assert isinstance(config.get('stages'),list)
for stage in config['stages']:
 assert all(isinstance(stage.get(key),str) and stage[key] for key in ('cat','title','image'))
(root/'store-config.js').write_text('window.STORE_CONFIG = '+json.dumps(config,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
print('Konfiguracja etapów gotowa.')
