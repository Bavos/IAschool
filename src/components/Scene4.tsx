import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame, spring, useVideoConfig } from 'remotion';
import { SceneData } from '../types';

type Props = {
  scene: SceneData;
};

export const Scene4: React.FC<Props> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const scale = spring({ frame, fps, config: { damping: 12 } });

  return (
    <AbsoluteFill style={{
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'flex-start',
      padding: '80px',
      textAlign: 'left',
      backgroundColor: scene.backgroundColor,
      color: scene.textColor,
      background: `linear-gradient(135deg, ${scene.backgroundColor} 0%, #000000 100%)`,
      fontFamily: 'sans-serif'
    }}>
      <div style={{ opacity, transform: `scale(${scale})` }}>
        <h1 style={{ fontSize: '70px', fontWeight: 'bold', marginBottom: '30px', color: scene.accentColor }}>{scene.title}</h1>
        <h2 style={{ fontSize: '40px', opacity: 0.9, marginBottom: '40px' }}>{scene.subtitle}</h2>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {scene.bullets.map((bullet, idx) => (
            <li key={idx} style={{ fontSize: '32px', marginBottom: '20px', display: 'flex', alignItems: 'center' }}>
              <span style={{ color: scene.accentColor, marginRight: '20px' }}>⚡</span> {bullet}
            </li>
          ))}
        </ul>
      </div>
    </AbsoluteFill>
  );
};
