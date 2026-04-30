import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, spring, useVideoConfig } from 'remotion';
import { SceneData } from '../types';

type Props = {
  scene: SceneData;
};

export const Scene5: React.FC<Props> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const scale = spring({ frame, fps, config: { damping: 12 } });

  return (
    <AbsoluteFill style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '80px',
      textAlign: 'center',
      backgroundColor: scene.backgroundColor,
      color: scene.textColor,
      background: `linear-gradient(135deg, ${scene.backgroundColor} 0%, #000000 100%)`,
      fontFamily: 'sans-serif'
    }}>
      <div style={{ opacity, transform: `scale(${scale})` }}>
        <h1 style={{ fontSize: '90px', fontWeight: 'bold', marginBottom: '30px', color: scene.accentColor }}>{scene.title}</h1>
        <h2 style={{ fontSize: '45px', opacity: 0.9, marginBottom: '50px' }}>{scene.subtitle}</h2>
        <p style={{ fontSize: '42px', fontWeight: 'bold', lineHeight: 1.4, color: scene.accentColor }}>
          {scene.body}
        </p>
      </div>
    </AbsoluteFill>
  );
};
