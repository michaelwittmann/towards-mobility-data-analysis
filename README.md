# Towards Mobility Data Analysis
This is a collection of Notebooks and examples and tutorials regarding mobility data analysis

# Run our Notebooks
Juypter Notebooks, are great for data analysis scripts. With this docker images, you can easily start a Jupyter server for mobility data analysis on your local machine or on a remote host. 

## Clone this repository into your home directory

```bash
cd ~
git clone https://github.com/michaelwittmann/towards-mobility-data-analysis.git
```
## Environment
### Install dependecies
```bash
poetry install
```

### Or use our prebuilt Docker image for mobility data analysis
Pull the latetst version of our docker image
```bash 
docker pull micwittmann/data-analysis-environment:python3.8-with-dependencies
```

Start jupyter server
- Set a password, or a token if you are on a machine which is accecible in your local network
```bash
docker run -p 8888:8888 -v ~/towards-mobility-data-analysis:/home/ubuntu/ --name jupyter-server micwittmann/data-analysis-environment:python3.8-with-dependencies jupyter notebook --allow-root --ip=0.0.0.0 --no-browser --NotebookApp.token='' --NotebookApp.password=''
```

# Contributors
- [Michael Wittmann](https://github.com/michaelwittmann)
- [Lennart Adenaw](https://github.com/ladenaw)
