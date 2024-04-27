import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The neural multilingual voice can speak different languages based on the input text.
speech_config.speech_synthesis_voice_name='ko-KR-SunHiNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = """
    AI의 미래는 다양한 기술 발전, 사회적 수용, 윤리적 고민 등 여러 요소에 의해 지속적으로 변화하고 발전할 것입니다. 여기 몇 가지 주요 방향성을 살펴보겠습니다:

### 1. **기술적 발전**
- **일반 인공지능 (AGI)**: 현재의 인공지능은 대부분 특정 작업에 최적화된 좁은 AI(Narrow AI)입니다. 미래에는 인간의 인지 능력을 모방하거나 넘어서는 일반 인공지능(AGI)의 개발이 진행될 수 있습니다.
- **언어 모델의 진화**: GPT와 같은 대형 언어 모델은 점점 더 고도화되어 자연스러운 대화, 복잡한 문제 해결, 창의적 작업 등을 수행할 수 있게 될 것입니다.
- **강화학습**: 실제 환경과 유사한 시뮬레이션을 통해 AI가 스스로 학습하고 최적의 행동을 결정하는 강화학습 기술이 발전할 것입니다.

### 2. **응용 분야의 확장**
- **의료**: 질병 진단, 치료 계획 수립, 수술 로봇 등 다양한 의료 분야에서 AI의 활용이 증가할 것입니다.
- **자동차**: 자율 주행 기술의 발전으로 인해 운전자 없는 차량이 일반화될 수 있습니다.
- **제조업**: AI와 로봇 기술의 결합으로 스마트 공장이 보다 효율적이고 생산적으로 변화할 것입니다.
- **금융**: 알고리즘 트레이딩, 개인화된 금융 조언, 리스크 관리 등에서 AI의 사용이 확대될 것입니다.

### 3. **윤리적, 법적 고려사항**
- **프라이버시**: 개인의 데이터를 활용하는 AI 기술은 프라이버시 보호와 데이터 보안에 대한 중요성을 증가시킬 것입니다.
- **고용 변화**: AI와 자동화로 인해 일부 직업은 사라지고, 새로운 형태의 일자리가 생겨날 것입니다. 이에 따른 사회적 적응이 필요할 것입니다.
- **규제**: 정부와 국제 기구에서 AI의 발전과 활용에 대한 규제를 마련하여 관리할 것입니다.

### 4. **사회적 도전**
- **격차의 심화**: 기술 접근성에서의 불평등이 커질 수 있으며, 이는 경제적, 교육적 격차를 심화시킬 수 있습니다.
- **인간과의 상호작용**: AI가 인간의 일상생활과 직업에 깊숙이 통합될수록, 인간과 AI의 상호작용 방식에 대한 연구와 이해가 더욱 중요해질 것입니다.

### 5. **교육과 훈련**
- **기술 교육**: AI 기술의 발전에 따라 관련 기술 교육이 중요해질 것이며, 평생 교육이 일반화될 가능성이 큽니다.

미래의 AI는 사회 구조와 인간 생활을 혁신적으로 바꿀 잠재력을 가지고 있습니다. 이러한 변화는 기술적 진보뿐만 아니라 윤리적, 법적, 교육적 측면에서의 깊은 성찰과 준비가 필요합니다.
"""
text.replace("-","").replace("#","").replace("*","")
print(text)
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")