import gpt_2_simple as gpt2

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
