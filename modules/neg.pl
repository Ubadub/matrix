#!/usr/bin/perl

# Perl script for customizing module handling sentential
# negation.  We'll eventually probably want just one big
# perl/cgi thing which handles all of the modules.  Negation
# seemed like a good place to start, since there are too
# many choices to just build separate .tdl files in this case.

# usage: perl neg.pl

print "What is the pathname for your Matrix directory?\n\n";
$answer = <STDIN>;
chomp($answer);
$matrix_dir = $answer;

unless (-e $matrix_dir."/lkb/script") {
#    die "There's something wrong with the Matrix stored in $matrix_dir.\n";
    print "There's something wrong with the Matrix stored in $matrix_dir.\n";
    print "I'm trying /home/bender/lingo/grammars/matrix\n\n";
    $matrix_dir = "/home/bender/lingo/grammars/matrix";
}

print "This questionnaire will help you build a prototype\n analysis of negation for your grammar.\n\n";

print "Does your language handle sentential negation by means of:\n\n";
print "\t a) inflection on the main verb\n";
print "\t b) an adverb\n";
print "\t c) both\n";
print "\t d) neither\n\n";

$answer = <STDIN>;
chomp($answer);

while ($answer =~ /^[^ABCDabcd]/) {
    print "Please type A B C or D.\n";
    $answer = <STDIN>;
    chomp($answer);
}

if ($answer =~ /^[Aa]/) {

    &generate_infl_neg;

} elsif ($answer =~ /^[Bb]/) {
    
    &generate_adv_neg;

} elsif ($answer =~ /^[Dd]/) {
    
    print "Sorry, I can't help you with negation today.\n";

} elsif ($answer =~ /^[Cc]/) {

    print "You've said your language has both inflectional sentential\n";
    print "negation and adverbial sentential negation.  Which scenario\n";
    print "best describes your language?\n\n";

    print "\t a) inflectional negation and adverbial negation are in\n\t\t"."complementary distribution\n";
    print "\t b) the inflectional negation and the adverb can appear\n\t\t"."independently or together\n";
    print "\t c) sentential negation requires both the inflection and\n\t\t"."the adverb\n";
    print "\t d) none of the above\n\n";
      

    $answer = <STDIN>;
    chomp($answer);

    while ($answer =~ /^[^ABCDabcd]/) {
	print "Please type A B C or D.\n";
	$answer = <STDIN>;
	chomp($answer);
    }

    if ($answer =~ /^[Aa]/) {

	&generate_infl_neg;
	&generate_adv_neg; 

    } elsif ($answer =~ /^[Bb]/) {

	&generate_infl_neg;
	&generate_adv_neg; 
	&generate_both_neg;

    } elsif ($answer =~ /^[Cc]/) {

	&generate_both_neg;

    } elsif ($answer =~ /^[Dd]/) {

	print "Sorry, I can't help you with negation today.\n";
	
    } 
}

#################################################################
# Subroutines

sub generate_infl_neg {

    print "Alright, let's work on inflectional negation.\n";
    print "Is the negation affix a prefix or a suffix?\n";
    $answer = <STDIN>;
    chomp($answer);

    while ($answer =~ /^[^PpSs]/) {
	print "Please type P or S.\n";
	$answer = <STDIN>;
	chomp($answer);
    }
   
    if ($answer =~ /^[Pp]/) {

	$affix = "prefix";

    } else {

	$affix = "suffix";

    }


    print "How is the negation $affix spelled in the underlying form?\n";
    print "Suggested form: NEG\n";

    $spelling = <STDIN>;
    chomp($spelling);

    &check_clobber("infl-neg-irule.tdl");

    open(OUTPUT,">$matrix_dir"."/modules/infl-neg-irule.tdl") || 
	die "Cannot create matrix/modules/infl-neg-irule.tdl.\n";

    print OUTPUT "\;\;\; -*- Mode: TDL; Package: LKB -*-\n\n";
    print OUTPUT "\;\;\; Autogenerated inflection negation module\n";
    print OUTPUT "\;\;\; Use in conjunction with infl-neg.tdl\n\n";

    print OUTPUT "neg-lr :=\n";
    print OUTPUT "%"."$affix (* $spelling)\n";
    print OUTPUT "negation-lex-rule.\n\n";

    print "Be sure to load infl-neg.tdl and infl-neg-irule.tdl in your script.\n\n";

}

sub generate_adv_neg {

    #Here we're going to have worry about whether or not the
    #scopal head-adj rules are already instantiated.  Hmmm...

    print "Generating tdl files for adverbial sentential negation.\n";
    print "Be sure to load adv-neg.tdl, adv-neg-lex.tdl, and adv-neg-rules.tdl in your script.\n\n";

}

sub generate_both_neg {

    print "Generating tdl files for two-part negation (inflection and adverb in the same sentence.\n";
    print "Be sure to load two-part-neg.tdl, two-part-neg-lex.tdl, two-part-neg-irule.tdl and two-part-neg-rules.tdl in your script.\n\n";

}

sub check_clobber {

    my($file) = $matrix_dir."/modules/".$_[0];

#    print "Calling check clobber on $file\n";

    if (-e $file) {

	print "$_[0] already exists. Continue anyway? [yn]";
	$answer = <STDIN>;
	chomp($answer);
	if ($answer =~ /^[Yy]$/) {
	    
	    print "Okay, continuing and overwriting output file...\n";
	    
	} else {
	    
	    print "Okay, quitting...\n";
	    exit (0);

	}
    }
}