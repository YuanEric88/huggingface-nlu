export MAX_LENGTH=128
export BERT_MODEL=bert-base-uncased
export OUTPUT_DIR=germeval-model-crf
export BATCH_SIZE=8
export NUM_EPOCHS=10
export SAVE_STEPS=50
export SEED=1

python3 run_ner.py --data_dir ./ \
--model_type bert_crf \
--labels ./labels.txt \
--model_name_or_path $BERT_MODEL \
--output_dir $OUTPUT_DIR \
--max_seq_length  $MAX_LENGTH \
--num_train_epochs $NUM_EPOCHS \
--per_gpu_train_batch_size $BATCH_SIZE \
--save_steps $SAVE_STEPS \
--seed $SEED \
--do_train \
--do_eval \
--do_predict
