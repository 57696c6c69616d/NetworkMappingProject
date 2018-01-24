<?php

namespace NMP\Form\Type;

use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\Extension\Core\Type\ChoiceType;

class MachineType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('ip', TextType::class)
            ->add('type', ChoiceType::class, array('choices' => array('U - Unknown' => 'U', 'C - Client' => 'C', 'F - Firewall' => 'F', 'R - Router' => 'R', 'S - Server' => 'S'), ));
    }

    public function getName()
    {
        return 'machine';
    }
}