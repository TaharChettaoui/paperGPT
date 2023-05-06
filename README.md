## PaperGPT
Using python and openai’s GPT to summarize papers.  
Inspired by a blog post, I decided to build upon the provided code, to add features, and improve code quality, speed as well as performance.  
You can also find a clear setup tutorial so that YOU can also start using this code in under 5 minutes!  

## Setup
In order to summarize your paper, you first need to specify some parameters in the "src/main.py".

+ Paper **arXiv** URL
+ OpenAI organization and API key:  
After creating an OpenAI account, you can find the Organization ID under "https://platform.openai.com/account/org-settings"  
Concerning the API key, you can create one under "https://platform.openai.com/account/api-keys"  

After filling in the previous pieces of information, you are good to go!

## Example
Here is an example for the "Proximal Policy Optimization Algorithms" paper:

> We propose a new family of policy gradient methods, called Proximal Policy Optimization (PPO), which alternates between sampling data through interaction with the environment, and optimizing a “surrogate” objective function using stochastic gradient ascent. PPO outperforms other online policy gradient methods, and overall strikes a favorable balance between sample complexity, simplicity, and wall-time.  
 TRPO maximizes a "surrogate" objective, LCPI(θ), which is the expected return under the current policy. To prevent excessively large policy updates, TRPO modifies the objective to LCLIP(θ), which clips the probability ratio at 1-ε and 1+ε and takes the minimum of the clipped and unclipped objective. This provides a lower bound on the unclipped objective.  
 We propose a new approach for improving the performance of policy gradient algorithms, by using a clipped surrogate objective or a KL penalty to ensure that the policy updates do not deviate too far from the initial policy. Our approach is simple to implement and can be used with any existing policy gradient algorithm. We demonstrate the effectiveness of our approach on several continuous control tasks.  
 We compare several different surrogate objectives under different hyperparameters. We find that clipping and penalty methods perform better than the no clipping or penalty objective.  
 We compared PPO to several other algorithms on continuous control tasks, and found it to  
We introduced Proximal Policy Optimization (PPO), a family of policy optimization methods that use multiple epochs of stochastic gradient ascent to perform each policy update. These methods have the stability and reliability of trust-region methods but are much simpler to implement, applicable in more general settings, and have better overall performance. We evaluated PPO on the Roboschool and Arcade Learning Environment benchmarks and found it to outperform other algorithms.  
PPO hyperparameters used for the Mujoco 1 million timestep benchmark include a horizon of 2048, Adam stepsize of 3 10 4, 10 epochs, minibatch size of 64, discount factor of 0.99, GAE parameter of 0.95. For the Roboschool experiments, the hyperparameters include a horizon of 512, Adam stepsize adjusted based on the target value of the KL divergence, 15 epochs, minibatch size of 4096, discount factor of 0.99, GAE parameter of 0.95, and number of actors of 32 (locomotion) and 128 (flagrun). For the Atari experiments, the hyperparameters include a horizon of 128, Adam stepsize of 2.5 10 4, 3 epochs, minibatch size of 32 8, discount factor of 0.99, GAE parameter of 0.95, number of actors of 8, clipping parameter of 0.1, and VF coeff. c (9) and entropy coeff. c (9) of 1 and 0.01 respectively.  
PPO and A2C both performed well on the 49 ATARI games included in OpenAI Gym at the time of publication. PPO outperformed A2C on some games, while A2C outperformed PPO on others.  
The mean final scores of PPO and A2C on Atari games after 40M game frames (10M time steps) are shown in Table 6.  

## Ref
https://medium.com/geekculture/a-paper-summarizer-with-python-and-gpt-3-2c718bc3bc88
