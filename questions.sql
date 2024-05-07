SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `questions`
--

-- --------------------------------------------------------

--
-- Structure de la table `questions`
--

CREATE TABLE IF NOT EXISTS `questions` (
  `question_id` int(10) unsigned NOT NULL,
  `question_label` varchar(100) NOT NULL,
  `question_type` varchar(30) NOT NULL,
  `difficulty` int(10) unsigned DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Structure de la table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `question_id` int(10) unsigned NOT NULL,
  `correct_answer` varchar(100) NOT NULL,
  `wrong_answer_1` varchar(100) NOT NULL,
  `wrong_answer_2` varchar(100) NOT NULL,
  `wrong_answer_3` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Structure de la table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(10) unsigned NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;




--
-- Contenu de la table `questions`
--

INSERT INTO `questions` (`question_id`, `question_label`, `question_type`, `difficulty`) VALUES
(1, 'Quelle est la capitale de la Turquie ?', 'Geographie', 2),
(4, 'Quelle est la traduction de "loathsome" ?', 'Langues', 3),
(3, 'Quelle est la valeur de x si 4x - 2 = 6 ?', 'Maths', 1),
(2, 'Quelle est la taille de la Tour Eiffel ?', 'Histoire', 3);

--
-- Contenu de la table `answers`
--

INSERT INTO `answers` (`question_id`, `correct_answer`, `wrong_answer_1`, `wrong_answer_2`, `wrong_answer_3`) VALUES
(1, 'Ankara', 'Istanbul', 'Balayra', 'Edirne'),
(4, 'détéstable', 'adorable', 'fainéant', 'logique'),
(3, '2', '4', '5', '0,5'),
(2, '330', '250', '420', '270');


--
-- Index pour les tables exportées
--

--
-- Index pour la table `questions`
--
ALTER TABLE `questions`
 ADD PRIMARY KEY (`question_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
