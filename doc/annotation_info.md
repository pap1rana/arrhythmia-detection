### svdb - MIT-BIH Supraventricular Arrhythmia Database
* annotated all heartbeats

### mitdb - MIT-BIH Arrhythmia Database
* annotated all heartbeats

### nsrdb - MIT-BIH Normal Sinus Rhythm Database
* annotated all heartbeats

### ltdb - MIT-BIH Long-Term ECG Database
* annotated all heartbeats

### vfdb - MIT-BIH Malignant Ventricular Fibrillation Database
* has custom annotations 
* some of them overlap with general annotations
* not all beats are annotated - best way to fix?

| Code       | Description                             |
|------------|-----------------------------------------|
| AFIB       | atrial fibrillation                     |
| ASYS       | asystole                                |
| B          | ventricular bigeminy                    |
| BI         | first degree heart block                |
| HGEA       | high grade ventricular ectopic activity |
| N or NSR   | normal sinus rhythm                     |
| NOD        | nodal ("AV junctional") rhythm          |
| NOISE      | noise                                   |
| PM         | pacemaker (paced rhythm)                |
| SBR        | sinus bradycardia                       |
| SVTA       | supraventricular tachyarrhythmia        |
| VER        | ventricular escape rhythm               |
| VF or VFIB | ventricular fibrillation                |
| VFL        | ventricular flutter                     |
| VT         | ventricular tachycardia                 |


### General annotation info

| Code | Description                                                                        |
|------|------------------------------------------------------------------------------------|
| N    | Normal beat (displayed as "·" by the PhysioBank ATM, LightWAVE, pschart, and psfd) |
| L    | 	Left bundle branch block beat                                                     |
| R    | 	Right bundle branch block beat                                                    |
| B    | 	Bundle branch block beat (unspecified)                                            |
| A    | 	Atrial premature beat                                                             |
| a    | 	Aberrated atrial premature beat                                                   |
| J    | 	Nodal (junctional) premature beat                                                 |
| S    | 	Supraventricular premature or ectopic beat (atrial or nodal)                      |
| V    | 	Premature ventricular contraction                                                 |
| r    | 	R-on-T premature ventricular contraction                                          |
| F    | 	Fusion of ventricular and normal beat                                             |
| e    | 	Atrial escape beat                                                                |
| j    | 	Nodal (junctional) escape beat                                                    |
| n    | 	Supraventricular escape beat (atrial or nodal)                                    |
| E    | 	Ventricular escape beat                                                           |
| /    | 	Paced beat                                                                        |
| f    | 	Fusion of paced and normal beat                                                   |
| Q    | 	Unclassifiable beat                                                               |
| ?    | 	Beat not classified during learning                                               |

Non-beat annotations:

| Code | Description                               |
|------|-------------------------------------------|
| [		  | Start of ventricular flutter/fibrillation |
| !		  | Ventricular flutter wave                  |
| ]		  | End of ventricular flutter/fibrillation   |
| x		  | Non-conducted P-wave (blocked APC)        |
| (		  | Waveform onset                            |
| )		  | Waveform end                              |
| p		  | Peak of P-wave                            |
| t		  | Peak of T-wave                            |
| u		  | Peak of U-wave                            |
| `		  | PQ junction                               |
| '		  | J-point                                   |
| ^		  | (Non-captured) pacemaker artifact         |
| \|   | Isolated QRS-like artifact                |
| ~		  | Change in signal quality                  |
| +		  | Rhythm change                             |
| s		  | ST segment change                         |
| T		  | T-wave change                             |
| *		  | Systole                                   |
| D		  | Diastole                                  |
| =		  | Measurement annotation                    |
| "		  | Comment annotation                        |
| @		  | Link to external data                     |

Rhythm annotations appear below the level used for beat annotations:

| Code   | Description                      |
|--------|----------------------------------|
| (AB	   | Atrial bigeminy                  |
| (AFIB	 | Atrial fibrillation              |
| (AFL	  | Atrial flutter                   |
| (B	    | Ventricular bigeminy             |
| (BII	  | 2° heart block                   |
| (IVR	  | Idioventricular rhythm           |
| (N	    | Normal sinus rhythm              |
| (NOD	  | Nodal (A-V junctional) rhythm    |
| (P	    | Paced rhythm                     |
| (PREX	 | Pre-excitation (WPW)             |
| (SBR	  | Sinus bradycardia                |
| (SVTA	 | Supraventricular tachyarrhythmia |
| (T	    | Ventricular trigeminy            |
| (VFL	  | Ventricular flutter              |
| (VT	   | Ventricular tachycardia          |

Signal quality and comment annotations appear above the level used for beat annotations:

| Code | Description                                                                                                                                                                            |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| qq	  | Signal quality change: the first character ('c' or 'n') indicates the quality of the upper signal (clean or noisy), and the second character indicates the quality of the lower signal |
| U	   | Extreme noise or signal loss in both signals: ECG is unreadable                                                                                                                        |
| M    | (or MISSB)	Missed beat                                                                                                                                                                 |
| P    | (or PSE)	Pause                                                                                                                                                                         |
| T    | (or TS)	Tape slippage                                                                                                                                                                  |