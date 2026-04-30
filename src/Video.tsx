import React from 'react';
import { Series } from 'remotion';
import { SceneData } from './types';
import { Scene1 } from './components/Scene1';
import { Scene2 } from './components/Scene2';
import { Scene3 } from './components/Scene3';
import { Scene4 } from './components/Scene4';
import { Scene5 } from './components/Scene5';

type VideoProps = {
  scenes: SceneData[];
};

export const VideoPrincipal: React.FC<VideoProps> = ({ scenes }) => {
  return (
    <Series>
      <Series.Sequence durationInFrames={scenes[0].durationInFrames}><Scene1 scene={scenes[0]} /></Series.Sequence>
      <Series.Sequence durationInFrames={scenes[1].durationInFrames}><Scene2 scene={scenes[1]} /></Series.Sequence>
      <Series.Sequence durationInFrames={scenes[2].durationInFrames}><Scene3 scene={scenes[2]} /></Series.Sequence>
      <Series.Sequence durationInFrames={scenes[3].durationInFrames}><Scene4 scene={scenes[3]} /></Series.Sequence>
      <Series.Sequence durationInFrames={scenes[4].durationInFrames}><Scene5 scene={scenes[4]} /></Series.Sequence>
    </Series>
  );
};
