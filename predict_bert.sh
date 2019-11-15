export MAX_LENGTH=128
export BERT_MODEL=bert-base-uncased
export OUTPUT_DIR=np-model-bert
export BATCH_SIZE=32
export NUM_EPOCHS=6
export SAVE_STEPS=750
export SEED=1

python3 run_ner.py --data_dir ./small_size_data/ \
--model_type bert \
--labels ./labels.txt \
--model_name_or_path $BERT_MODEL \
--output_dir $OUTPUT_DIR \
--max_seq_length  $MAX_LENGTH \
--num_train_epochs $NUM_EPOCHS \
--per_gpu_train_batch_size $BATCH_SIZE \
--save_steps $SAVE_STEPS \
--seed $SEED \
--overwrite_output_dir \
--do_predict \
--online_predict True
