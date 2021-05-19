import gpt_2_simple as gpt2
import os.path
import gdown
if not os.path.isfile("run2.tar"):
  url = 'https://drive.google.com/u/0/uc?id=1T5BntQPxoRjGDMAUbqUwUnsDs2DARM6C&export=download'#You can set your to your own model on gdrive
  #ok but this is run2.tar
  #not shakespeare.txt, so how to train your own
  #good question https://github.com/minimaxir/gpt-2-simple or https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce
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
def generate(prefixs="nexity"):
  return gpt2.generate(sess,
                    length=250,
                    temperature=0.7,
                    prefix=prefixs,
                    nsamples=5,
                    batch_size=5,
                    run_name=runName
                    )
