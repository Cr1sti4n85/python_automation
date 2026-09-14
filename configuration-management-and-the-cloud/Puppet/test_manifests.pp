describe 'gksu', :type => :class do
  let (:facts) { { 'is_virtual' => 'false' } }
  it { should contain_package('gksu').with_ensure('latest') }
end

/*
This code runs an rspec test to determine whether the gksu package has the intended behavior when the fact is_virtual is set to false. When this is the case, the gksu package should have the ensure parameter set to latest: ensure('latest')
*/