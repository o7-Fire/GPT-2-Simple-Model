import gpt_2_simple as gpt2
import os.path
import gdown
if not os.path.isfile("run2.tar"):
  url = 'https://drive.google.com/uc?id=0B9P1L--7Wd2vNm9zMTJWOGxobkU'
  output = 'run2.tar'
  gdown.download(url, output, quiet=False)
  print("")
  return
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
