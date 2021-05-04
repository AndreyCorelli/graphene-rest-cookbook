#!/usr/bin/env bash
sudo docker build -t graphene-cookbook .
sudo docker save -o ./graphene-cookbook.tar graphene-cookbook
