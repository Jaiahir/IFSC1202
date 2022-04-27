function[]=turtle(comd)
floor= char (32*ones (20,20));

k = 0;

x = -1;

c = 0;

rn = 20;

cn = 1;
i=1
while i <= length (comd):
    switch comd(i):
        case 1:
            k = 0;
        case 2:
            k = 1;
        case 3:
            if c==0:
                c=-r
                r=0
            else:
                r=0
                c=0
            end
        case 4:
            if c==0:
                c=r;
                r=0;
            else:
                r=-c;
                c=0;
            end
        case 5:
            i=i+1;
            if k == 1:
                if c == 0:
                    if r== 1:
                        floor (rn + 1:rn + comd (i), cn) = '*';
                    else:
                        floor (rn - comd (i): rn - 1, cn) = '*';
                    end
                    rn = rn + r*comd (i);
            else:
                if c==1:
                     floor (rn ,cn+1: cn+ comd (i)) = '*';
                else:
                    floor (rn , cn-comd (i):cn-1) = '*';
                end
                cn=cn+c*comd(i);
            end
        else:
            if c==0:
                rn=rn+r*comd(i)
            else:
                cn=cn+c*comd(i)
            end
        end
    case 6:
        disp(floor)
    otherwise:
        break
    end
    i=i+1
end