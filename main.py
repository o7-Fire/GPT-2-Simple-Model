import gpt_2_simple as gpt2
import os.path
import gdown
if not os.path.isfile("run2.tar"):
  url = 'https://drive.google.com/u/0/uc?id=1T5BntQPxoRjGDMAUbqUwUnsDs2DARM6C&export=download'#You can set your to your own model on gdrive
  output = 'run2.tar'
  print("Downloading pretrained model...")
  gdown.download(url, output, quiet=False)
  print("Untar run2.tar")
  exit(0)
runName = "run2"
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=runName)
print(gpt2.generate(sess,
                    length=250,
                    temperature=0.7,
                    prefix="Fuhrer",
                    nsamples=5,
                    batch_size=5,
                    run_name=runName
                    ))
