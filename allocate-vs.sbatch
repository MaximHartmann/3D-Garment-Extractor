#!/bin/bash
#SBATCH --job-name="vs"
#SBATCH --partition=day
#SBATCH --time=04:00:00
#SBATCH --gres=gpu:A4000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G

/usr/sbin/sshd -D -p 7777 -f /dev/null -h $HOME/.ssh/id_ecdsa
