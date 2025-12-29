require 'wav-file'

wav = open("Assignment1.wav")
format = WavFile::readFormat(wav)
# <WavFile::Format:0x007f872a034860 @id=1, @channel=2, @hz=44100, @bytePerSec=176400, @blockSize=4, @bitPerSample=16> 
chunk = WavFile::readDataChunk(wav)

wav.close