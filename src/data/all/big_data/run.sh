#../../../gibbs-lda-couple/src/lda -est -alpha 0.2 -beta 0.1 -beta_t 0.2 -beta_g 0.2 -ntopics 10 -ntimes 8 -ngeos 10 -niters 100 -savestep 101 -twords 20 -dfile tv_p_dfile.txt.mini -dfile_t tv_p_dfile_t.txt.mini -dfile_g tv_p_dfile_g.txt.mini


topics=100

../../../gibbs-lda/src/lda -est -alpha 1 -beta 0.05  -ntopics $topics -niters 100 -savestep 101 -twords 20 -dfile data_set/training.txt

m_d=model_1_0.05_"$topics"

mkdir -p  $m_d

mv data_set/model-final.*  $m_d/


mv data_set/wordmap.txt  $m_d/
