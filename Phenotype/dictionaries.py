phenotype_dict = {"PosteriorGap": "Posterior Gap", "LateralGap": "Lateral Gap",
                  "BazookaExclusion": "Bazooka excluded", "Par1atPosterior": "Par1 at Posterior", "Nucleus": "Nucleus Position"}


# label order for Par1; Jup
par1_order = [{'PosteriorGap': 'No', 'LateralGap': 'No', 'Par1atPosterior': 'Yes'},
              {'PosteriorGap': 'No', 'LateralGap': 'Yes', 'Par1atPosterior': 'Yes'},
              {'PosteriorGap': 'Yes', 'LateralGap': 'Yes', 'Par1atPosterior': 'Yes'},
              {'PosteriorGap': 'Yes', 'LateralGap': 'Yes', 'Par1atPosterior': 'No'}
              ]


# label order for Baz; Jup
baz_order = [{'PosteriorGap': 'No', 'LateralGap': 'No', 'BazookaExclusion': 'No'},
             {'PosteriorGap': 'No', 'LateralGap': 'Yes', 'BazookaExclusion': 'No'},
             {'PosteriorGap': 'No', 'LateralGap': 'Yes', 'BazookaExclusion': 'Yes'},
             {'PosteriorGap': 'Yes', 'LateralGap': 'Yes', 'BazookaExclusion': 'Yes'},
             {'PosteriorGap': 'Yes', 'LateralGap': 'Yes', 'BazookaExclusion': 'No'}
             ]
