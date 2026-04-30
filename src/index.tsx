import { Composition, registerRoot } from "remotion";
import { VideoPrincipal } from "./Video";
import { SceneData } from "./types";
import sceneData from "../data/sceneData.json";

const scenes = sceneData as SceneData[];
const totalDuration = scenes.reduce((acc, s) => acc + s.durationInFrames, 0);

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="VideoPrincipal"
      component={VideoPrincipal}
      durationInFrames={totalDuration}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={{ scenes }}
    />
  );
};

registerRoot(RemotionRoot);
