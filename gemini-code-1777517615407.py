import os
import json

def setup():
    # Directories
    for d in ["src/components", "data", "public/images", ".github/workflows"]:
        os.makedirs(d, exist_ok=True)
    
    # Types
    with open("src/types.ts", "w") as f:
        f.write('export type SceneData = { id: string; type: string; title: string; subtitle: string; body: string; bullets: string[]; durationInFrames: number; backgroundColor: string; textColor: string; accentColor: string; imagePrompt: string; imageUrl: string; animation: string; transition: string; layout: string; };\n')

    # index.tsx
    with open("src/index.tsx", "w") as f:
        f.write('import { Composition, registerRoot } from "remotion";\nimport { VideoPrincipal } from "./Video";\nimport { SceneData } from "./types";\nimport sceneData from "../data/sceneData.json";\nconst scenes = sceneData as SceneData[];\nconst totalDuration = scenes.reduce((acc, s) => acc + s.durationInFrames, 0);\nexport const RemotionRoot: React.FC = () => (\n  <Composition id="VideoPrincipal" component={VideoPrincipal} durationInFrames={totalDuration} fps={30} width={1080} height={1920} defaultProps={{ scenes }} />\n);\nregisterRoot(RemotionRoot);\n')

    # Video.tsx
    with open("src/Video.tsx", "w") as f:
        f.write('import React from "react";\nimport { Series } from "remotion";\nimport { SceneData } from "./types";\nimport { Scene1 } from "./components/Scene1";\nimport { Scene2 } from "./components/Scene2";\nimport { Scene3 } from "./components/Scene3";\nimport { Scene4 } from "./components/Scene4";\nimport { Scene5 } from "./components/Scene5";\ntype VideoProps = { scenes: SceneData[] };\nexport const VideoPrincipal: React.FC<VideoProps> = ({ scenes }) => (\n  <Series>\n    <Series.Sequence durationInFrames={scenes[0].durationInFrames}><Scene1 scene={scenes[0]} /></Series.Sequence>\n    <Series.Sequence durationInFrames={scenes[1].durationInFrames}><Scene2 scene={scenes[1]} /></Series.Sequence>\n    <Series.Sequence durationInFrames={scenes[2].durationInFrames}><Scene3 scene={scenes[2]} /></Series.Sequence>\n    <Series.Sequence durationInFrames={scenes[3].durationInFrames}><Scene4 scene={scenes[3]} /></Series.Sequence>\n    <Series.Sequence durationInFrames={scenes[4].durationInFrames}><Scene5 scene={scenes[4]} /></Series.Sequence>\n  </Series>\n);\n')

    # Scene Components
    for i in range(1, 6):
        with open(f"src/components/Scene{i}.tsx", "w") as f:
            f.write(f"import React from 'react';\nimport {{ AbsoluteFill, interpolate, useCurrentFrame }} from 'remotion';\nimport {{ SceneData }} from '../types';\nexport const Scene{i}: React.FC<{{ scene: SceneData }}> = ({{ scene }}) => {{\n  const frame = useCurrentFrame();\n  return (\n    <AbsoluteFill style={{\n      backgroundColor: scene.backgroundColor, color: scene.textColor,\n      display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '100px',\n      fontFamily: 'sans-serif', textAlign: 'center'\n    }}>\n      <h1 style={{ fontSize: '100px', color: scene.accentColor }}>{{scene.title}}</h1>\n      <h2 style={{ fontSize: '60px', marginBottom: '40px' }}>{{scene.subtitle}}</h2>\n      <p style={{ fontSize: '40px' }}>{{scene.body}}</p>\n      {{scene.bullets.map((b, idx) => <div key={{idx}} style={{ fontSize: '35px', marginTop: '10px' }}>• {{b}}</div>)}}\n    </AbsoluteFill>\n  );\n}};")

    # Configs
    with open("package.json", "w") as f:
        json.dump({
            "name": "iamazing-school",
            "scripts": {
                "preview": "remotion preview src/index.tsx",
                "render": "remotion render src/index.tsx VideoPrincipal out/video.mp4",
                "build": "tsc --noEmit"
            },
            "dependencies": {
                "remotion": "^4.0.0",
                "@remotion/cli": "^4.0.0",
                "react": "^18.0.0",
                "react-dom": "^18.0.0",
                "typescript": "^5.0.0"
            }
        }, f)
    
    with open("tsconfig.json", "w") as f:
        json.dump({"compilerOptions": {"target": "ES2020", "module": "ESNext", "lib": ["DOM", "ES2020"], "strict": True, "jsx": "react-jsx", "moduleResolution": "Node", "resolveJsonModule": True}}, f)
    
    with open("remotion.config.ts", "w") as f:
        f.write('import { Config } from "@remotion/cli/config";\nConfig.setVideoImageFormat("jpeg");\nConfig.setOverwriteOutput(true);\nConfig.setCodec("h264");\nConfig.setPixelFormat("yuv420p");\n')

    # Data
    scenes = [
        {"id": "s1", "type": "op", "title": "IA não é o futuro.", "subtitle": "É o agora.", "body": "A IAmazing mostra como usar inteligência artificial de um jeito simples, prático e aplicável.", "bullets": [], "durationInFrames": 120, "backgroundColor": "#050816", "textColor": "#ffffff", "accentColor": "#00ff99", "imagePrompt": "", "imageUrl": "", "animation": "fade", "transition": "smooth", "layout": "center"},
        {"id": "s2", "type": "ct", "title": "Todo mundo fala de IA.", "subtitle": "Poucos sabem usar de verdade.", "body": "A IAmazing conecta conhecimento, estratégia e prática para transformar IA em resultado real.", "bullets": [], "durationInFrames": 120, "backgroundColor": "#0a0e27", "textColor": "#ffffff", "accentColor": "#7000ff", "imagePrompt": "", "imageUrl": "", "animation": "slide", "transition": "smooth", "layout": "left"},
        {"id": "s3", "type": "ct", "title": "Aprender IA pode ser simples.", "subtitle": "Sem enrolação. Sem complicar.", "body": "Aqui, a tecnologia vira ferramenta de criação, produtividade e crescimento.", "bullets": [], "durationInFrames": 120, "backgroundColor": "#050816", "textColor": "#ffffff", "accentColor": "#00d4ff", "imagePrompt": "", "imageUrl": "", "animation": "zoom", "transition": "smooth", "layout": "center"},
        {"id": "s4", "type": "ft", "title": "O que você encontra na IAmazing", "subtitle": "Conhecimento aplicado para sair do zero.", "body": "", "bullets": ["IA aplicada ao crescimento", "Automações para ganhar produtividade", "Consultoria para tirar ideias do papel", "Educação prática e mão na massa", "Linguagem simples para aprender de verdade"], "durationInFrames": 150, "backgroundColor": "#0a0e27", "textColor": "#ffffff", "accentColor": "#00ff99", "imagePrompt": "", "imageUrl": "", "animation": "stagger", "transition": "smooth", "layout": "left"},
        {"id": "s5", "type": "cl", "title": "IAmazing School", "subtitle": "Sua entrada prática no mundo da IA.", "body": "Venha entender e aprender IA de maneira descomplicada e com muita mão na massa. IAMAZING SCHOOL", "bullets": [], "durationInFrames": 150, "backgroundColor": "#050816", "textColor": "#ffffff", "accentColor": "#7000ff", "imagePrompt": "", "imageUrl": "", "animation": "fade", "transition": "smooth", "layout": "center"}
    ]
    with open("data/sceneData.json", "w") as f:
        json.dump(scenes, f, indent=2)

    with open(".github/workflows/render.yml", "w") as f:
        f.write("name: Render\non: [push]\njobs:\n  render:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-node@v4\n        with: {node-version: 20}\n      - run: npm install\n      - run: npm run render\n")

setup()
print("Everything created.")